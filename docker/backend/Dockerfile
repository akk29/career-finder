FROM python:3.13.3-alpine
WORKDIR /usr/src/app
COPY ../../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ../../ .
EXPOSE 8000
RUN chmod +x ./docker/backend/server-entrypoint.sh
