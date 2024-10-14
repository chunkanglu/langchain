from typing import List

from langchain_core.tools import BaseTool
from langchain_core.tools.base import BaseToolkit

from langchain_community.tools.discord import (
    DiscordBanUser,
    DiscordDeleteMessage,
    DiscordGetMembers,
    DiscordGetMessages,
    DiscordGetUser,
    DiscordSendMessage,
)
from langchain_community.utilities.discord import DiscordAPIWrapper


class DiscordToolkit(BaseToolkit):
    """Toolkit for interacting with Discord."""

    tools: List[BaseTool] = []

    @classmethod
    def from_discord_api_wrapper(
        cls, discord_api_wrapper: DiscordAPIWrapper
    ) -> "DiscordToolkit":
        tools = [
            DiscordGetMessages(api_wrapper=discord_api_wrapper),
            DiscordSendMessage(api_wrapper=discord_api_wrapper),
            DiscordDeleteMessage(api_wrapper=discord_api_wrapper),
            DiscordGetMembers(api_wrapper=discord_api_wrapper),
            DiscordGetUser(api_wrapper=discord_api_wrapper),
            DiscordBanUser(api_wrapper=discord_api_wrapper),
        ]
        return cls(tools=tools)  # type: ignore[arg-type]

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
