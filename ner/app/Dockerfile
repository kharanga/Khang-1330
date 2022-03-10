FROM python:3.8

WORKDIR /code


RUN pip install requests
RUN pip3 install h2o-wave==0.16.0

COPY ./src /code/app
EXPOSE 10101
CMD ["uvicorn", "app.app:main", "--host", "0.0.0.0", "--port", "8000"]
