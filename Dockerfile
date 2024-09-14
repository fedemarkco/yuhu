FROM python:3.10.5-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/run.sh