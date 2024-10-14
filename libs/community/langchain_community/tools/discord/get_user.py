from typing import Optional

from langchain_core.callbacks import CallbackManagerForToolRun

from langchain_community.tools.discord.base import BaseDiscordTool


class DiscordGetUser(BaseDiscordTool):
    """Get a user' information from a Discord."""

    name: str = ...  # TODO
    description: str = ...  # TODO

    async def _run(self, run_manager: Optional[CallbackManagerForToolRun] = None):
        """Run the tool."""
        ...  # TODO
