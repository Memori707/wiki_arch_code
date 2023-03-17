from os import environ
from pydantic import BaseSettings

class DefaultSettingsLocal(BaseSettings):
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "/clown_service")
    APP_HOST: str = environ.get("APP_HOST", "127.0.0.1")
    APP_PORT: int = int(environ.get("APP_PORT", 8000))