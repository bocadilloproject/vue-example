from bocadillo import App, configure

from . import settings
from .router import router

app = App()
app.include_router(router)
configure(app, settings)
