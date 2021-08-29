docker-compose exec python /usr/local/bin/python flask db init
docker-compose exec python /usr/local/bin/python flask db migrate
docker-compose exec python /usr/local/bin/python flask db upgrade