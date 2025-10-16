"""
Main client for hh.ru SDK.
Provides root interface for working with HeadHunter.
"""

from hhru.auth import AnonymousAuthProvider
from hhru.backend import AbstractBackendProvider, BackendApiProvider, BackendProtocol


class Client(BackendProtocol):
    """
    ## hh.ru SDK client.
    Main entry point for working with HeadHunter.

    ### Example use:
    ```python
    import hhru
    client = hhru.Client(...)
    ```
    """

    def __init__(self, backend: AbstractBackendProvider | None = None) -> None:
        self.__steal_protocol(backend or BackendApiProvider(AnonymousAuthProvider()))

    def __steal_protocol(self, protocol: BackendProtocol) -> None:
        self.search_vacancies = protocol.search_vacancies
        self.search_vacancies_over_pages = protocol.search_vacancies_over_pages
