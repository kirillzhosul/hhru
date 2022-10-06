"""
    Main client for hh.ru SDK.
    Provides root interface for working with HeadHunter.
"""
from typing import Callable, Union, Dict, List, Optional


# Components.
from hhru.api import Api
from hhru.auth import Auth


class Client:
    """
    ## hh.ru SDK client.
    Main interface for working with HeadHunter.
    Provides auth, api interfaces.

    ### Example use:
    ```python
    import hhru
    client = hhru.Client()
    ```
    """

    # Authentication instance.
    # Used for authentication.
    auth = None

    # API instance.
    # Used for sending API HTTP requests.
    api = None

    def __init__(self):

        # Components.
        self.auth = Auth()
        self.api = Api(auth=self.auth)
