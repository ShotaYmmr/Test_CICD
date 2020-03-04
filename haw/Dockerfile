FROM python:3.8.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /haw
WORKDIR /haw
ADD requirements.txt /haw/
RUN pip install -r requirements.txt
ADD . /haw/
