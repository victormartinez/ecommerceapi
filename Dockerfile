FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code

WORKDIR /code

ADD . /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN useradd -ms /bin/bash "ecommerceuser"

USER ecommerceuser

EXPOSE 5000