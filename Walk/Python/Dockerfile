FROM python:3.12-alpine

ENV http_proxy http://10.255.46.226:3128
ENV https_proxy http://10.255.46.226:3128

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python main.py
