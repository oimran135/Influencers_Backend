#!/bin/bash
sudo docker exec -tiu postgres dreams_db_1 psql
sudo docker-compose exec web python manage.py migrate --noinput
