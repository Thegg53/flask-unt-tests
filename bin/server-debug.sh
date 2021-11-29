#!/bin/bash

export FLASK_APP=./mysrc/__init__.py
export FLASK_ENV=development

flask run --port 8085