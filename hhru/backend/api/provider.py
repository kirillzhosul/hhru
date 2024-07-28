from typing import Any, Generator, List

import requests

from hhru.auth.type import AuthAccessType
from hhru.backend.abstract import AbstractBackendProvider
from hhru.consts import VACANCY_SEARCH_MAX_PER_PAGE
from hhru.dto.vacancy import VacancyDTO

from .consts import API_TARGET_HOST, API_USER_AGENT
from .http_response import BackendApiResponse


class BackendApiProvider(AbstractBackendProvider):
    """
    Backend provider based on HTTP API

    Documentation: https://api.hh.ru/openapi/redoc
    """

    def _method(self, name: str, **kwargs: Any) -> BackendApiResponse:
        """
        Executes API method with given name and then returns response
        """

        headers = {"User-Agent": API_USER_AGENT}
        result = requests.get(f"{API_TARGET_HOST}/{name}", kwargs, headers=headers)
        response = BackendApiResponse(result)

        if response.status_code != 200:
            raise Exception(response.raw_json())  # TODO

        return response

    def search_vacancies(self, **kwargs: Any) -> List[VacancyDTO]:
        if self.auth_provider.access_type.value <= AuthAccessType.abstract.value:
            raise Exception("Access type should be non-abstract!")
        response = self._method("vacancies", **kwargs)
        return [VacancyDTO.model_validate(v) for v in response["items"]]

    def search_vacancies_over_pages(
        self, *, page_limit: int = 21, **kwargs: Any
    ) -> Generator[VacancyDTO, Any, None]:
        if self.auth_provider.access_type.value <= AuthAccessType.abstract.value:
            raise Exception("Access type should be non-abstract!")

        page = 0
        per_page = VACANCY_SEARCH_MAX_PER_PAGE

        while True:
            response = self._method("vacancies", page=page, per_page=per_page, **kwargs)
            items = [VacancyDTO.model_validate(v) for v in response["items"]]
            pages = response["pages"]
            page += 1

            yield from items
            if page >= pages or page >= page_limit:
                break
