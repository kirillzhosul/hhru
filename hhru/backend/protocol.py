from collections.abc import Generator
from typing import Any, Protocol

from hhru.dto import VacancyDTO


class BackendProtocol(Protocol):
    """
    Interface of backend methods
    """

    def search_vacancies(self, **kwargs: Any) -> list[Any]:
        """
        Returns list of search results for vacancies
        """
        raise NotImplementedError

    def search_vacancies_over_pages(
        self, *, page_limit: int = 21, **kwargs: Any
    ) -> Generator[VacancyDTO, Any, None]:
        """
        Returns list of search results for vacancies that was collected from all result pages (hh.ru has limit to 20 max pages search depth)
        """
        raise NotImplementedError


class AsyncBackendProtocol(Protocol):
    async def search_vacancies(self, **kwargs: Any) -> list[Any]: ...

    async def search_vacancies_async_burst(
        self, *, page_limit: int = 21, **kwargs: Any
    ) -> list[VacancyDTO]: ...
