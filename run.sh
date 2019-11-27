#!/usr/bin/env bash
echo 'starting MyhealthTornado project'
cd /usr/src/MyhealthTornado
git pull
pip install -r requirements.txt
cd /usr/src/MyhealthTornado/
gunicorn -w 1 -b 0.0.0.0:5000 -k tornado chat:application -D