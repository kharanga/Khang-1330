FROM python:3.8

COPY . /app

WORKDIR /app

RUN pip install requests
RUN pip3 install h2o-wave==0.16.0

EXPOSE 10101
CMD uvicorn --host="0.0.0.0" client:main --reload
