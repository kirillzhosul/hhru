from hhru.auth.type import AuthAccessType

from .abstract import AbstractAuthProvider


class DirectAuthProvider(AbstractAuthProvider):
    """
    TODO!
    """

    access_type: AuthAccessType = AuthAccessType.abstract

    login: str
    password: str

    def __init__(self, login: str, password: str, as_applicant: bool = True) -> None:
        super().__init__()
        if not as_applicant:
            raise NotImplementedError
        self.login = login
        self.password = password
