FROM python:3.4
MAINTAINER Nathan Bigaignon <nathanbigaignon@gmail.com>
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
