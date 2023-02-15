### Simple Todo App in Flask
A todo backend written in flask
#### Requirements
- Python3.10
- PIP


### Run Locally on a Linux Machine
```console
git clone https://github.com/axrav/_todoFlask
cd _todoFlask/todo_app
vim .env # fill with your values look onto sample.env
pip3 install -r requirements.txt
python3 -m gunicorn app:app --bind 0.0.0.0:${PORT} --workers 4 
## make sure you have set the port in env or use a port here
```

### Run using docker
```console
git clone https://github.com/axrav/_todoFlask
cd _todoFlask/todo_app
vim .env # fill with your values look onto sample.env
docker image build -t todo_image .
docker run -p {YOURPORT:YOURPORT} -d --name {name} -e PORT={YOURPORT} todo_image
```

### Tools used
- [Python3.10](https://www.python.org/downloads/release/python-3100/)
- [Mongodb](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)
- [PIP](https://pypi.org/project/pip/)
