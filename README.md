# Document Reader
​
​
## Installation
​

### Create a Virtual Environment
```sh
$ python3 -m venv env
```

### Start the created Virtual Environment (Linux)
```sh
$ . env/bin/activate
```

### Install with pip:
```sh
$ pip install -r requirements.txt
```
​
### Create a superuser
```sh
$ python manage.py createsuperuser
```

## Run Project
```sh
$ python manage.py runserver
```
​
## Endpoints
​
### For SMTP EMAIL
#### POST
```sh
/apis/smtp
````
​
### For SendGrid EMAIL
#### POST 
```sh
/apis/sendgrid
````
