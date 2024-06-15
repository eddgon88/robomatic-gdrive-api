# application/__init__.py
from fastapi import FastAPI
from .routers import apirouter
from . import config

app_configs = {"title": "test-executor-api",
               "HOST": config.HOST,
               "SA_CLIENT_ID": config.SA_CLIENT_ID}

def create_app():
    app = FastAPI(**app_configs)
    app.include_router(apirouter.router)
    return app
