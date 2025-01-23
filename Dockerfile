FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ ./src/

# Expose the port Flask runs on
EXPOSE 5000

CMD ["gunicorn", "--chdir", "/app/src/shared/infra/http", "--bind", "0.0.0.0:5000", "server:app"]
