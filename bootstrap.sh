#!/bin/sh
export FLASK_APP=./src/index.py
export FLASK_DEBUG=True
source .venv/bin/activate
flask run -h 0.0.0.0 -p 9999 --debugger
