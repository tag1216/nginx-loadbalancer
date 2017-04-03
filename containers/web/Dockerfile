FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/usr/src/app

WORKDIR $APP_HOME

ADD ./requirements.txt $APP_HOME
RUN pip install -r requirements.txt
