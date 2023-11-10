# HIS_Project_Backend

setup:
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

or

docker-compose up

docker exec -it postgres bash
psql -h localhost -U user
CREATE DATABASE hisdb;


database schema:
https://drawsql.app/teams/aut-2/diagrams/his-database