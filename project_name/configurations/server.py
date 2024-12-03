from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from project_name.pkg.db.database import engine

from fastapi import FastAPI

from project_name.configurations.routes import __routes__
from project_name.internal.events.example_event import register_startup_event


class Server:

    __app = FastAPI()

    def __init__(self, app: FastAPI):

        self.__app = app
        self.__register_routes(app)
        self.__register_events(app)

    def get_app(self) -> FastAPI:

        return self.__app

    @staticmethod
    def __register_events(app):

        register_startup_event(app)

    @staticmethod
    def __register_routes(app):

        __routes__.register_routes(app)
