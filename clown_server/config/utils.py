from os import environ

from clown_server.config.default import DefaultSettingsLocal


def get_settings() -> DefaultSettingsLocal:
    env = environ.get("ENV")
    if env == "local":
        return DefaultSettingsLocal()
    # ...
    # space for other settings
    # ...
    return DefaultSettingsLocal()