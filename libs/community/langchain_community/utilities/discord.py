"""Util that calls Discord."""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Dict

from langchain_core.utils import get_from_dict_or_env
from pydantic import BaseModel, model_validator

if TYPE_CHECKING:
    import discord


class DiscordAPIWrapper(BaseModel):
    """Wrapper for Discord API."""

    discord_client: Any = None
    discord_token: str = None

    @model_validator(mode="before")
    @classmethod
    def validate_environment(cls, values: Dict) -> dict:
        """Validate environment."""
        try:
            import discord
        except ImportError as e:
            raise ImportError(
                f"Could not import discord python package. "
                f"Please install it with `pip install -U discord.py`."
            ) from e

        discord_token = get_from_dict_or_env(values, "discord_token", "DISCORD_TOKEN")
        # TODO: other needed configurations here

        if not discord_token:
            # TODO: link to discord instructions
            raise ValueError(
                "Error: DISCORD_TOKEN environment variable has not been set. "
            )

        values["discord_client"] = discord.Client(intents=discord.Intents.default())
        values["discord_token"] = discord_token

        return values

    @asynccontextmanager
    async def create_connection(self):
        """Context manager for automatically setting up and closing the connection.

        Can be used to wrap each call to the Discord API for tools in this wrapper class.

        Example:
        ```
        async with self.create_connection():
            # do something with the Discord API
        ```
        """
        await self.discord_client.login(self.discord_token)
        try:
            yield
        finally:
            await self.discord_client.close()
