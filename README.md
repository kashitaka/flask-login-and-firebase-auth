# flask-login and Firebase Authentication

This is example implementation of Flask-login and Firebase Authentication

## Run

```bash
pip install -U pipenv
pipenv install
FLASK_APP=web pipenv run flask
```

## API without login

```bash
curl http://localhost:5000/login_not_required
```

It returns...
```bash
{"result":"ok"}
```

## login required API

```bash
curl -H X-Auth-Token:eyJhbXXXXXXXX....... http://localhost:5000/login_required
```

It returns... 
```bash
{"result":"ok","user_id":"XXXXXXXXXX"}
```

If you request with invalid firebase authentication token. then it returns
```bash
{"result":"unauthorized"}
```
