echo killing old docker processes
# docker-compose rm -fs 
docker-compose stop

echo building docker containers
# docker-compose up --build -d --remove-orphans
docker-compose up --build --remove-orphans
