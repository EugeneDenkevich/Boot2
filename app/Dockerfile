FROM python:3.11.4-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /opt/app

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools wheel

COPY ./requirements.txt /opt/app/requirements.txt
RUN pip install -r /opt/app/requirements.txt

COPY . /opt/app/app

EXPOSE 8000

RUN cd ..

CMD ["uvicorn", "app:create_app", "--host", "0.0.0.0", "--port", "8000"]