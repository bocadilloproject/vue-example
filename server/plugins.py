import orm
from bocadillo import App, HTTPError


def use_orm(app: App):
    @app.error_handler(orm.NoMatch)
    async def on_no_match(req, res, exc):
        raise HTTPError(404)
