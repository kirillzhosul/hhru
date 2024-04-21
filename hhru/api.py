"""
    API class for working with API (HTTP).
    Sends HTTP requests, handles API methods.
"""

from typing import Any, Optional

import requests

from hhru.auth import Auth
from hhru.response import Response


class Api:
    """
    Wrapper for API methods, HTTP sender.
    """

    # URL of the API.
    _api_server_provider_url = "https://api.hh.ru"

    def __init__(self, auth: Optional[Auth] = None) -> None:
        """
        :param auth: Auth provider as the `Auth` instance.
        """
        if auth and not isinstance(auth, Auth): # type: ignore
            raise TypeError(
                "Auth must be an instance of `Auth`! You may not pass auth as it will be initialise blank internally in `Api`."
            )
        self._auth = auth if auth else Auth()

    def method(
        self,
        name: str,
        **kwargs: Any,
    ) -> Response:
        """
        Executes API method with given name.
        And then return response from it.
        :param name: Name of the method to call.
        """

        # Build URL where API method is located.
        api_server_method_url = f"{self._api_server_provider_url}/{name}"
        http_params = kwargs.copy()

        # Send HTTP request.
        http_response = requests.get(url=api_server_method_url, params=http_params, headers={"User-Agent": self._auth.user_agent})

        # Wrap HTTP response in to own Response object.
        response = Response(http_response=http_response)

        return response
