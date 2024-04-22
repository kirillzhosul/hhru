"""
hh.ru SDK library.
SDK Library for HeadHunter API.
Provides interface for working with HeadHunter.
HH website: https://hh.ru/
HH API endpoint: https://apihh.ru/

HH developer documentation:
- https://github.com/hhru/api
- https://api.hh.ru/openapi/redoc

Author && Maintainer:
- Kirill Zhosul (@kirillzhosul)
- kirillzhosul@yandex.com
- https://github.com/kirillzhosul
"""

from hhru import consts
from hhru.auth import AbstractAuthProvider, AnonymousAuthProvider, AuthAccessType
from hhru.backend import AbstractBackendProvider, BackendApiProvider
from hhru.client import Client

__all__ = [
    "AbstractBackendProvider",
    "BackendApiProvider",
    "AuthAccessType",
    "AbstractAuthProvider",
    "AnonymousAuthProvider",
    "Client",
    "consts",
]
