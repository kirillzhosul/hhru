from hhru.auth.type import AuthAccessType

from .abstract import AbstractAuthProvider


class AnonymousAuthProvider(AbstractAuthProvider):
    """
    Provider without any information, used in base requests like vacancies search
    """

    access_type: AuthAccessType = AuthAccessType.anonymous
