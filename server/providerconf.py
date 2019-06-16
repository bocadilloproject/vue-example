# blog/providerconf.py
from bocadillo import provider
from .models import database


@provider(scope="app")
async def db():
    async with database:
        yield database
