FROM python:3.13.3-alpine
RUN set -ex \
    && apk update \
    && pip3 install --upgrade pip
WORKDIR /app
COPY ../../backend/ .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
# RUN chmod +x ./docker/backend/server-entrypoint.sh
RUN ["python", "manage.py", "makemigrations"]
RUN ["python", "manage.py", "migrate"]
RUN ["python", "manage.py", "collectstatic", "--noinput"]
CMD ["gunicorn", "CareerFinder.wsgi", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "4"]