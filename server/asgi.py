from bocadillo import App, configure, discover_providers

from . import settings
from .router import router

discover_providers("server.providerconf")

app = App()
app.include_router(router)
configure(app, settings)
