from typing import Any, Generator, List, Protocol


class BackendProtocol(Protocol):
    """
    Interface of backend methods
    """

    def search_vacancies(self, **kwargs: Any) -> List[Any]:
        """
        Returns list of search results for vacancies
        """
        raise NotImplementedError

    def search_vacancies_over_pages(
        self, *, page_limit: int = 21, **kwargs: Any
    ) -> Generator[Any, Any, None]:
        """
        Returns list of search results for vacancies that was collected from all result pages (hh.ru has limit to 20 max pages search depth)
        """
        raise NotImplementedError
