from bocadillo import App, Request, Response

app = App()


@app.route("/urls")
class Urls:
    async def post(self, req: Request, res: Response):
        res.json = {"message": "TODO"}
        res.status_code = 201
