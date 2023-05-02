FROM python:3.7-slim
RUN mkdir /app
COPY requirements.txt /app
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip3 install psycopg2 \
    && pip3 install -r /app/requirements.txt --no-cache-dir
COPY api_yamdb/ /app 
WORKDIR /app
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 
