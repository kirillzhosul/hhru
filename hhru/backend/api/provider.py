import asyncio
from asyncio import Semaphore
from collections.abc import AsyncGenerator, Generator
from types import CoroutineType
from typing import Any

import requests
from aiohttp import ClientSession

from hhru.auth.providers.abstract import AbstractAuthProvider
from hhru.auth.type import AuthAccessType
from hhru.backend.abstract import AbstractBackendProvider
from hhru.backend.abstract.abstract import AbstractAsyncBackendProvider
from hhru.consts import VACANCY_SEARCH_MAX_PER_PAGE
from hhru.dto.vacancy import VacancyDTO

from .consts import API_TARGET_HOST, API_USER_AGENT


class BackendApiProvider(AbstractBackendProvider):
    """
    Backend provider based on HTTP API

    Documentation: https://api.hh.ru/openapi/redoc
    """

    def __init__(
        self,
        auth_provider: AbstractAuthProvider,
        api_url: str = API_TARGET_HOST,
    ) -> None:
        super().__init__(auth_provider)
        self.api_host = api_url

    def _method(self, name: str, **kwargs: Any) -> dict[str, Any]:
        """
        Executes API method with given name and then returns response
        """

        headers = {"User-Agent": API_USER_AGENT}
        result = requests.get(f"{self.api_host}/{name}", kwargs, headers=headers)

        if result.status_code != 200:
            raise Exception(result.text)  # TODO

        return result.json()

    def search_vacancies(self, **kwargs: Any) -> list[VacancyDTO]:
        if self.auth_provider.access_type.value <= AuthAccessType.abstract.value:
            raise Exception("Access type should be non-abstract!")
        response = self._method("vacancies", **kwargs)
        return [VacancyDTO.model_validate(v) for v in response["items"]]

    def search_vacancies_over_pages(
        self, *, page_limit: int = 21, **kwargs: Any
    ) -> Generator[VacancyDTO]:
        if self.auth_provider.access_type.value <= AuthAccessType.abstract.value:
            raise Exception("Access type should be non-abstract!")

        page = 0
        per_page = VACANCY_SEARCH_MAX_PER_PAGE

        while True:
            response = self._method("vacancies", page=page, per_page=per_page, **kwargs)
            items = (VacancyDTO.model_validate(v) for v in response["items"])
            pages = response["pages"]
            page += 1

            yield from items
            if page >= pages or page >= page_limit:
                break


class BackendAsyncApiProvider(AbstractAsyncBackendProvider):
    semaphore: asyncio.Semaphore

    def __init__(
        self,
        auth_provider: AbstractAuthProvider,
        api_url: str = API_TARGET_HOST,
        concurrent_max_requests: int = 10,
    ) -> None:
        super().__init__(auth_provider=auth_provider)
        self.semaphore = asyncio.Semaphore(concurrent_max_requests)
        self.api_host = api_url

    async def _method(
        self, name: str, semaphore: Semaphore, **kwargs: Any
    ) -> dict[str, Any]:
        """
        Executes API method with given name and then returns response
        """

        headers = {"User-Agent": API_USER_AGENT}

        async with (
            semaphore,
            ClientSession() as session,
            session.get(
                f"{self.api_host}/{name}",
                params=kwargs,
                headers=headers,
                ssl=False,
            ) as req,
        ):
            if req.status != 200:
                raise Exception(await req.text())  # TODO
            return await req.json()

    async def search_vacancies(self, **kwargs: Any) -> list[VacancyDTO]:
        if self.auth_provider.access_type.value <= AuthAccessType.abstract.value:
            raise Exception("Access type should be non-abstract!")
        response = await self._method("vacancies", **kwargs, semaphore=self.semaphore)
        return [VacancyDTO.model_validate(v) for v in response["items"]]

    async def search_vacancies_over_pages(
        self, *, page_limit: int = 21, **kwargs: Any
    ) -> AsyncGenerator[VacancyDTO]:
        if self.auth_provider.access_type.value <= AuthAccessType.abstract.value:
            raise Exception("Access type should be non-abstract!")

        page = 0
        per_page = VACANCY_SEARCH_MAX_PER_PAGE

        while page < page_limit:
            response = await self._method(
                "vacancies", page=page, per_page=per_page, **kwargs
            )
            items = (VacancyDTO.model_validate(v) for v in response["items"])
            pages = response["pages"]
            page += 1

            for item in items:
                yield item

            if page >= pages:
                break

    async def search_vacancies_async_burst(
        self, *, page_limit: int = 21, **kwargs: Any
    ) -> list[VacancyDTO]:
        if self.auth_provider.access_type.value <= AuthAccessType.abstract.value:
            raise Exception("Access type should be non-abstract!")

        per_page = VACANCY_SEARCH_MAX_PER_PAGE

        initial_response = await self._method(
            "vacancies",
            page=0,
            semaphore=self.semaphore,
            per_page=per_page,
            **kwargs,
        )

        responses = [initial_response]
        pages = initial_response["pages"]

        coroutines: list[CoroutineType[Any, Any, dict[str, Any]]] = []
        for page in range(1, min(page_limit, pages)):
            coroutine = self._method(
                "vacancies",
                page=page,
                per_page=per_page,
                **kwargs,
                semaphore=self.semaphore,
            )
            coroutines.append(coroutine)

        responses += await asyncio.gather(*coroutines)

        vacancies = [
            VacancyDTO.model_validate(v)
            for response in responses
            for v in response["items"]
        ]

        return vacancies
