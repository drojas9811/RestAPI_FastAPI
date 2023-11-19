FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

ENV PYTHONUNBUFFERED True

RUN apt-get clean && apt-get update
RUN apt-get install -y locales locales-all

COPY requirements.txt ./
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app/src

WORKDIR /app/src
EXPOSE 8080
ARG WORKERS_UVICORN
ENV WORKERS=$WORKERS_UVICORN
RUN echo ${WORKERS}

CMD ["sh", "-c","uvicorn src.main:app --host 0.0.0.0 --port 8080 ${WORKERS}"]