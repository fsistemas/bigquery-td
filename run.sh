#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/service-account.json"

echo $GOOGLE_APPLICATION_CREDENTIALS

python app.py
