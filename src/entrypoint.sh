#!/bin/sh
set -ex

# Start gunicorn, listening on port 500, access log to stdout
exec uvicorn main:app --reload --port 5000 --host 0.0.0.0
