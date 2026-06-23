#!/bin/sh
set -eu

if [ -n "${BACKEND_HOST:-}" ] && [ -n "${BACKEND_PORT:-}" ]; then
  export BACKEND_URL="http://${BACKEND_HOST}:${BACKEND_PORT}"
fi

case "${BACKEND_URL:-}" in
  ""|http://127.0.0.1:8000)
    echo "ERROR: Configure BACKEND_URL on the frontend Railway service."
    echo "Example: BACKEND_URL=https://learning-app-production-a732.up.railway.app"
    ;;
  *)
    echo "Frontend will proxy /api to: ${BACKEND_URL}"
    ;;
esac
