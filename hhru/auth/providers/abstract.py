from abc import ABC

from hhru.auth.type import AuthAccessType


class AbstractAuthProvider(ABC):
    """
    Not implemented auth provider,
    used in providers hierarchy
    """

    access_type: AuthAccessType = AuthAccessType.abstract
