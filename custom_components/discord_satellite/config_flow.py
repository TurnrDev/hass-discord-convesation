import voluptuous as vol

from homeassistant import config_entries
from .const import DOMAIN

DATA_SCHEMA = vol.Schema({vol.Required("token"): str})

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 0
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Discord Satellite", data=user_input)
        
        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA, errors={})