#!/usr/bin/env bash
# Simple wait script

until nc -z $1 $2; do
  echo "⏳ Waiting for $1:$2 to be ready..."
  sleep 2
done

exec "${@:3}"
