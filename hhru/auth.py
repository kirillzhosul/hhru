"""
    Authentication DTO.
"""


from typing import Optional


class Auth:
    """
    Wrapper for authentication data.
    """


    def __init__(self, user_agent: Optional[str] = None):
        self._user_agent = user_agent or "hh.ru-python"

    @property
    def user_agent(self) -> str:
        return self._user_agent

    @user_agent.setter
    def user_agent(self, new: str) -> None:
        self._user_agent = new