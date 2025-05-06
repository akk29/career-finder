# Career Finder

Find you next career job with career finder

## Dependencies

[![Python](https://img.shields.io/badge/python-3.13.3-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3133/)
[![Django Web Framework](https://img.shields.io/badge/django-5.2-blue.svg?style=flat-square)](https://pypi.org/project/Django/5.2/)



### 1. Steps for setting project

```shell
# get source code
git clone https://github.com/akk29/career-finder

# go inside directory
cd career-finder

# install, create virtualenv and activate virtualenv (optional)
python -m venv .venv
.venv\Scripts\activate # windows
source .venv/bin/activate # linux

# install requirements
pip install -r requirements.txt

# run development server locally
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

# create super user
# stop the server
python manage.py createsuperuser
```

### 2. Steps for running project via docker


```shell
docker compose up
```

Visit : http://127.0.0.1:8000 in your browser for project

Visit : http://127.0.0.1:8000/admin for default admin portal
