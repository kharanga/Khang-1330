FROM python:3.8

WORKDIR /code
RUN python -m pip install --upgrade pip

RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm

RUN pip install fastapi==0.74.0
RUN pip install "uvicorn[standard]"==0.17.5

COPY ./app /code/app
EXPOSE 8000
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]
