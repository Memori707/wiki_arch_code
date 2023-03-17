from fastapi import FastAPI
from uvicorn import run

from clown_server.config import *


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "Микросервиc по заказу клоунов."

    application = FastAPI(
        title="API clown_server",
        description=description,
        docs_url="/swagger",
        version="1.0.0",
    )
    settings = get_settings()
    application.state.settings = settings
    return application

app = get_app()