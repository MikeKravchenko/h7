## How to run it right now:

* reload.sh

# OR:

* docker build -t imageh7 .
* docker run -d --name mycontainer123 -p 80:80 imageh7
* docker exec -it mycontainer123 bash
* python3 h7server.py

## To do list:

To make it wor with Auth0:
- expose (gcp?)
- call by autho0 webhook
- your login + user's data for hl7 <> auth0 <> webhook <> deployed app

Security:
- https
- white list for auth0 only
- (optional) static token
