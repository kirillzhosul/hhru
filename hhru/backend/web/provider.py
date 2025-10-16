import requests

from hhru.auth import AbstractAuthProvider, DirectAuthProvider
from hhru.backend import AbstractBackendProvider, BackendApiProvider

from .consts import WEB_DEFAULT_AUTH_HEADERS, WEB_TARGET_HOST


class BackendWebProvider(AbstractBackendProvider):
    """
    Backend provider based on web interface
    """

    def __init__(self, auth_provider: AbstractAuthProvider) -> None:
        super().__init__(auth_provider)

        self.__steal_api_implementations()

        self._web_session = requests.session()
        self.__login_session()

    def __steal_api_implementations(self) -> None:
        """
        Some implementations are not required to be on web,
        so we steal them from API protocol
        """
        api_provider = BackendApiProvider(self.auth_provider)
        self.search_vacancies = api_provider.search_vacancies
        self.search_vacancies_over_pages = api_provider.search_vacancies_over_pages

    def get_xsrf_from_cookies(self) -> str | None:
        for p in self._web_session.cookies.items():  # type: ignore
            if p[0] == "_xsrf":
                return p[1]  # type: ignore

    def __login_session(self):
        if not isinstance(self.auth_provider, DirectAuthProvider):
            raise Exception("Web backend requires `DirectAuthProvider`!")

        path = f"{WEB_TARGET_HOST}/account/login"
        params = {"backurl": "/", "hhtmFrom": "main"}

        self._web_session.headers.update(WEB_DEFAULT_AUTH_HEADERS)
        self._web_session.get(path, params=params)

        xsrf = self.get_xsrf_from_cookies()

        data = {
            "_xsrf": xsrf,
            "backUrl": "https://hh.ru/",
            "failUrl": "/account/login?backurl=%2F",
            "remember": "yes",
            "username": {self.auth_provider.login},
            "password": {self.auth_provider.password},
            "isBot": "false",
        }

        if not xsrf:
            raise Exception("No XSRF")
        self._web_session.headers.update({"x-xsrftoken": xsrf})
        response = self._web_session.post(path, params=params, data=data)

        if response.status_code != 200:
            raise Exception("Can`t login, wrong status!")

        if "recaptcha" in response.text:
            raise Exception("Can`t login, captcha raised, not supported!")

        raise NotImplementedError
