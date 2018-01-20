FROM ubuntu:14.04

RUN apt-get update && apt-get install -y python-pip python-dev && apt-get clean

RUN pip install bottle

EXPOSE 8080

ADD . /app
WORKDIR /app

