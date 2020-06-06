FROM tiangolo/uwsgi-nginx-flask:python3.8 

COPY ./app /app
RUN chmod +rwx /app
RUN cd /app && python3 -m pip install -r requirements.txt
WORKDIR /app
# CMD ["python3", "h7server.py", "&"]