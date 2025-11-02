from hhru.auth.providers.abstract import AbstractAuthProvider
from hhru.backend.protocol import AsyncBackendProtocol, BackendProtocol


class AbstractBackendProvider(BackendProtocol):
    """
    Not implemented backend provider,
    used in providers hierarchy
    """

    auth_provider: AbstractAuthProvider

    def __init__(self, auth_provider: AbstractAuthProvider) -> None:
        super().__init__()
        self.auth_provider = auth_provider


class AbstractAsyncBackendProvider(AsyncBackendProtocol):
    """
    Not implemented async backend provider,
    used in providers hierarchy
    """

    auth_provider: AbstractAuthProvider

    def __init__(self, auth_provider: AbstractAuthProvider) -> None:
        super().__init__()
        self.auth_provider = auth_provider
