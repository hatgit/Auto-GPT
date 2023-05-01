# sourcery skip: do-not-use-staticmethod
"""
A module that contains the Singleton class object that creates a singleton instance of the AIConfig class
"""
from __future__ import annotations

from typing import Any, Type

import wrapt

from autogpt.config.ai_config import AIConfig


@wrapt.decorator
def singleton(wrapped: Type[AIConfig], instance: Any = None) -> Type[AIConfig]:
    """
    A decorator that creates a singleton instance of the wrapped class.

    Parameters:
        wrapped (Type[AIConfig]): The class to be wrapped.
        instance (Any): The instance of the wrapped class.

    Returns:
        Type[AIConfig]: The singleton instance of the wrapped class.
    """
    if instance is None:
        instance = wrapped()
    return instance


@singleton
class Singleton(AIConfig):
    """
    A class object that creates a singleton instance of the AIConfig class.

    Attributes:
        ai_name (str): The name of the AI.
        ai_role (str): The description of the AI's role.
        ai_goals (list): The list of objectives the AI is supposed to complete.
        api_budget (float): The maximum dollar value for API calls (0.0 means infinite)
    """

    def __init__(
        self,
        ai_name: str = "",
        ai_role: str = "",
        ai_goals: list | None = None,
        api_budget: float = 0.0,
    ) -> None:
        """
        Initialize a class instance

        Parameters:
            ai_name (str): The name of the AI.
            ai_role (str): The description of the AI's role.
            ai_goals (list): The list of objectives the AI is supposed to complete.
            api_budget (float): The maximum dollar value for API calls (0.0 means infinite)
        Returns:
            None
        """
        super().__init__(ai_name, ai_role, ai_goals, api_budget)


singleton_instance = Singleton.load()


__all__ = ["singleton_instance"]
