"""
    Main client for hh.ru SDK.
    Provides root interface for working with HeadHunter.
"""
from typing import Callable, Union, Dict, List, Optional


# Components.
from hhru.api import Api
from hhru.auth import Auth
from hhru.consts import VACANCY_SEARCH_MAX_PER_PAGE


class Client:
    """
    ## hh.ru SDK client.
    Main interface for working with HeadHunter.
    Provides auth, api interfaces.

    ### Example use:
    ```python
    import hhru
    client = hhru.Client()
    ```
    """

    # Authentication instance.
    # Used for authentication.
    auth = None

    # API instance.
    # Used for sending API HTTP requests.
    api = None

    def __init__(self):

        # Components.
        self.auth = Auth()
        self.api = Api(auth=self.auth)

    def search_vacancies(self, **kwargs) -> List:
        """Returns list of search results for vacancies"""
        response = self.api.method(name="vacancies", **kwargs)
        return response.items

    def search_vacancies_over_pages(self, *, page_limit: int = 21, **kwargs) -> List:
        """Returns list of search results for vacancies that was collected from all result pages (hh.ru has limit to 20 max pages search depth)."""
        search_current_page = 0
        while True:
            response = self.api.method(
                name="vacancies",
                page=search_current_page,
                per_page=VACANCY_SEARCH_MAX_PER_PAGE,
                **kwargs,
            )
            search_current_page += 1
            if response.raw_response().status_code != 200:
                # Temporary solution.
                print(response.raw_json())
                raise Exception
            for item in response.items:
                yield item
            if (
                search_current_page >= response.pages
                or search_current_page >= page_limit
            ):
                break
