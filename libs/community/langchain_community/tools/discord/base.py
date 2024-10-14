"""Base class for Discord tools."""

from __future__ import annotations

from typing import TYPE_CHECKING

from langchain_core.tools import BaseTool
from pydantic import Field

from langchain_community.utilities.discord import DiscordAPIWrapper

if TYPE_CHECKING:
    import discord


class BaseDiscordTool(BaseTool):
    """Base class for Discord tools."""

    api_wrapper: DiscordAPIWrapper = Field(default_factory=DiscordAPIWrapper)
    """The Discord client object."""
