from typing import TYPE_CHECKING, List

from langchain_core.tools import BaseTool
from langchain_core.tools.base import BaseToolkit

from langchain_community.utilities.discord import DiscordAPIWrapper
from langchain_community.tools.discord import (
    DiscordGetMessages,
    DiscordGetMembers,
    DiscordSendMessage,
    DiscordDeleteMessage,
    DiscordGetUser,
    DiscordBanUser,
)

if TYPE_CHECKING:
    import discord


class DiscordToolkit(BaseToolkit):
    """Toolkit for interacting with Discord."""

    @classmethod
    def from_discord_api_wrapper(cls, discord_api_wrapper: DiscordAPIWrapper) -> "DiscordToolkit":
        tools = [
            DiscordGetMessages(api_wrapper=discord_api_wrapper),
            DiscordSendMessage(api_wrapper=discord_api_wrapper),
            DiscordDeleteMessage(api_wrapper=discord_api_wrapper),
            DiscordGetMembers(api_wrapper=discord_api_wrapper),
            DiscordGetUser(api_wrapper=discord_api_wrapper),
            DiscordBanUser(api_wrapper=discord_api_wrapper),
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
