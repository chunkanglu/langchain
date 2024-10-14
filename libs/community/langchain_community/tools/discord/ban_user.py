from typing import Optional

from langchain_core.callbacks import CallbackManagerForToolRun

from langchain_community.tools.discord.base import BaseDiscordTool


class DiscordBanUser(BaseDiscordTool):
    """Ban a user from a Discord Guild/Server."""

    name: str = ...  # TODO
    description: str = ...  # TODO

    async def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None):
        """Run the tool."""
        ...  # TODO
