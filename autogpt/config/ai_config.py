# sourcery skip: do-not-use-staticmethod
"""
A module that contains the AIConfig class object that loads the configuration from a file
"""
from __future__ import annotations

import json
from typing import Any, Dict


class AIConfig:
    """
    A class object that loads the configuration from a file.

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
        self.ai_name = ai_name
        self.ai_role = ai_role
        self.ai_goals = ai_goals or []
        self.api_budget = api_budget

    @staticmethod
    def load(file_path: str = "config.json") -> AIConfig:
        """
        Load the configuration from a file.

        Parameters:
            file_path (str): The path to the configuration file.

        Returns:
            AIConfig: The configuration object.
        """
        try:
            with open(file_path, "r") as f:
                config_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            config_data = {}

        return AIConfig(
            ai_name=config_data.get("ai_name", ""),
            ai_role=config_data.get("ai_role", ""),
            ai_goals=config_data.get("ai_goals", []),
            api_budget=config_data.get("api_budget", 0.0),
        )
