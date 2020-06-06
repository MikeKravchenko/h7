## How to run it right now :

* docker build -t imageh7 .
* docker run -d --name mycontainer123 -p 80:80 imageh7
* docker exec -it mycontainer123 bash
* python3 h7server.py