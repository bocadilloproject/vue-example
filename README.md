# bocadillo-vue-example

URL Shortener web app built with [Bocadillo] and [Vue.js].

[bocadillo]: https://bocadilloproject.github.io
[vue.js]: https://vuejs.org

![](media/demo.gif)

## Project structure

- `server/`: a REST API server built with [Bocadillo], including [orm](https://github.com/encode/orm) for data validation and database storage, and [hashids](https://github.com/davidaurelio/hashids-python) for URL hash generation.
- `frontend/`: a Single-Page Application built with [Vue.js], [Vue Router](https://router.vuejs.org) and [Bulma](https://bulma.io).

## Install

You will need [Python](https://www.python.org/) 3.6+ and [Node.js](https://nodejs.org/en/).

### Backend

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Frontend

Run `cd frontend` first, then:

```bash
npm install
```

### Database

Database support is provided by [Databases](https://github.com/encode/databases), and dependencies for **PostgreSQL** and **SQLite** are installed by default (see `requirements.txt`).

However, note that the backend connects to the database via a `DATABASE_URL`, so it is **database-agnostic**.

You can provide the `DATABASE_URL` via an environment variable, or in a `.env` file located at the project root directory, e.g.:

```bash
# PostgreSQL:
DATABASE_URL="postgresql://localhost:5432/urlshortener"

# OR, for SQLite:
DATABASE_URL="sqlite:///sqlite.db"
```

## Quickstart

Start the Bocadillo backend app from the project root directory using:

```bash
uvicorn server.asgi:app
```

It will be running at http://localhost:8000.

In another terminal, run `cd frontend` and then start the Vue frontend using:

```bash
npm start
```

You can access it at http://localhost:8080.

Happy URL shortening!

## License

MIT
