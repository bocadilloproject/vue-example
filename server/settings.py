from starlette.config import Config
from starlette.datastructures import URL

from .plugins import use_orm

config = Config(".env")

CORS = {
    "allow_origins": ["http://localhost:8080"],
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
DATABASE_URL = config("DATABASE_URL", cast=URL)
PLUGINS = [use_orm]
