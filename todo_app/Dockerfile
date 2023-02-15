FROM python:3.10-slim-bullseye

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["sh", "-c", "python3 -m gunicorn app:app --bind 0.0.0.0:${PORT} --workers 4"]