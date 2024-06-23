FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

COPY . /app

EXPOSE 80

RUN mkdir ~/.streamlit

RUN cp config.toml ~/.streamlit/config.toml

RUN cp credentials.toml ~/.streamlit/credentials.toml

WORKDIR /app

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]