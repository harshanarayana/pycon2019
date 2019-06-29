FROM python:3.7-slim
MAINTAINER Harsha Narayana


# Start Installing the Basic Dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn

RUN mkdir -p /sanic/config
RUN mkdir -p /sanic/bootiful_sanic

COPY config/* /sanic/config/
COPY bootiful_sanic/ /sanic/bootiful_sanic/
COPY requirements.txt /sanic
COPY run.py /sanic/run.py
COPY .env /sanic/.env

WORKDIR /sanic
RUN find . -type f

ENV SANIC_SERVER_PORT 8000
ENV SANIC_SERVER_HOST 0.0.0.0

EXPOSE 8000


ENTRYPOINT ["python", "run.py"]

