FROM python:3.11.4-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools wheel

COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt

COPY . /opt/app/app

COPY wait-for-it.sh /wait-for-it.sh
COPY ./Makefile .
RUN chmod +x /wait-for-it.sh

EXPOSE 8000
