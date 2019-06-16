from starlette.config import Config

config = Config(".env")

CORS = {
    "allow_origins": ["http://localhost:8080"],
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
