#!/bin/sh

echo 'starting MyhealthTornado project'
cd /usr/src/MyhealthTornado
gunicorn -w 1 -b 0.0.0.0:8000 -k tornado chat:application -D
