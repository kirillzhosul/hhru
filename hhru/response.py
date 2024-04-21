"""
    Response class.
    Result of all API methods.
"""

from typing import Any, Dict

from requests import Response as HTTPResponse


class Response:
    """
    API response structure.
    """

    # Raw response fields.
    _raw_json: Dict[Any, Any]
    _raw_response: HTTPResponse

    def __init__(self, http_response: HTTPResponse):
        """
        :param http_response: Response object (HTTP).
        """

        # Store raw response to work later.
        self._raw_response = http_response

        # Parse raw response once for working later.
        self._raw_json = self._raw_response.json()

    def get(self, key: str, default: Any = None):
        """
        Allows to access Response fields by `response.get(field, default)`.
        """
        try:
            return self[key]
        except KeyError:
            return default

    def __getitem__(self, key: str) -> Any:
        """
        Allows to access Response fields by `response[field]`.
        Notice that this will fall with `KeyError` if field was not found in the response.
        """
        if key not in self._raw_json:
            raise KeyError(f"{key} does not exist in the response!")
        field_value = self._raw_json.get(key, None)
        return field_value

    def __getattr__(self, attribute_name: str) -> Any:
        """
        Allows to access Response fields by `response.my_response_var`.
        Notice that this will fall with `AttributeError` if field was not found in the response.
        """
        if attribute_name not in self._raw_json:
            raise AttributeError(f"{attribute_name} does not exist in the response!")
        attribute_value = self._raw_json.get(attribute_name, None)
        return attribute_value

    def raw_json(self) -> Dict[Any, Any]:
        """
        Returns raw JSON from the response.
        WARNING: Do not use this method.
        """
        return self._raw_json

    def raw_response(self) -> HTTPResponse:
        """
        Returns raw response object.
        WARNING: Do not use this method.
        """
        return self._raw_response
