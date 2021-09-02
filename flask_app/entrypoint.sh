#!/usr/bin/env bash
flask db init
flask db migrate
flask db upgrade
bash -c "gunicorn -w 1 -b 0.0.0.0:5000 run:app"