#!/bin/sh
set -eu

export BACKEND_URL="${BACKEND_URL:-http://backend:8000}"
export PORT="${PORT:-80}"

envsubst '${BACKEND_URL} ${PORT}' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf

exec nginx -g 'daemon off;'
