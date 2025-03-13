import asyncio

import discord
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_intents = discord.Intents.default()
_intents.message_content = True

_client = discord.Client(intents=_intents)


@asyncio.coroutine
async def async_setup(hass: HomeAssistant, config: ConfigType):
    async with _client:
        await _client.start(config["token"])
        discord.utils.setup_logging(root=False)