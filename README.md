# agni

This is simple API server for original information retrieval system.

One of the research topic of our laboratory is interface design to make them aware of something important.
This API helps you to concentrate on developing your own interface.

## Requirements

- python (^3.6.7)
- docker

## Run

The first time you have to build container with `--build` option.

- API server

```sh
cd app
docker compose up --build
```

- DB(MySQL)

```sh
cd database
docker compose up --build
```

Now you can see API server in `localhost:8888`, and MySQL server in `localhost:3336`.

Once you build container, you can run servers without `--build` option.

- API server

```sh
cd app
docker compose up
```

- DB(MySQL)

```sh
cd database
docker compose up
```

Of curse you can run w/o docker ;)

## Develop

1. Clone this repository.

2. Install dependencies.

In `/app` directory, there are dependency list files. (`pyproject.toml` and `requirements.txt`)

If you use [poetry](https://python-poetry.org/), run following command.

\* **Make sure you have compatible python environment. (3.6.7)**

```sh
poetry shell
poetry install
```

If not, install dependencies by using `requirements.txt` like

```sh
pip install -r requirements.txt
```

3. Edit as you like. 🎉
