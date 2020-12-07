FROM python:3.8-slim-buster

RUN pip install flask

ADD . /webster

CMD ["/webster/lookup.py"]

EXPOSE 5000
