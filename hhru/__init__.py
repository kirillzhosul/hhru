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

# Library specific information.
from hhru.__version__ import (
    __author__,
    __author_email__,
    __copyright__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
)

# Additional API.
from hhru.api import Api
from hhru.auth import Auth

# Base API.
from hhru.client import Client
from hhru.response import Response

__all__ = ["Api", "Auth", "Response", "Client", "consts"]
