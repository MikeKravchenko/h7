docker build -t imageh7 .
docker stop containerh7
docker rm containerh7
docker run -d --name containerh7 -p 80:80 imageh7
docker exec -it containerh7 python3 h7server.py