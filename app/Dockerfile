# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM python:3.7

COPY . /app

EXPOSE 8000

RUN python3 -m pip install -r /app/requirements.txt
