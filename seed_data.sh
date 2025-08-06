#!/bin/bash

rm -rf migrations
rm db.sqlite3
python manage.py makemigrations artisendapi
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
