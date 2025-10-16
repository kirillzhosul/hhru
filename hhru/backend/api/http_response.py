from collections.abc import Mapping
from typing import Any

from requests import Response


class BackendApiResponse:
    """
    Backend API response structure (JSON)
    """

    _raw_json: Mapping[str, Any]

    def __init__(self, response: Response) -> None:
        self._raw_response = response
        self._raw_json = self._raw_response.json()

    def get(self, key: str, default: Any = None) -> Any:
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

    def raw_json(self) -> Mapping[Any, Any]:
        """
        Returns raw JSON from the response.
        WARNING: Do not use this method.
        """
        return self._raw_json

    @property
    def status_code(self) -> int:
        """
        Returns HTTP status code of the request
        """
        return self._raw_response.status_code
