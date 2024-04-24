#!/bin/sh

# Execute the FastAPI application using uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8080 $WORKERS --log-config ./app/log_conf.yaml
