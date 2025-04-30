# Career Finder

Find you next career job with career finder

## Dependencies

[![Python](https://img.shields.io/badge/python-3.13.3-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3133/)
[![Django Web Framework](https://img.shields.io/badge/django-4.2.0-blue.svg?style=flat-square)](https://pypi.org/project/Django/4.2.0/)



### 1. Steps for setting project

```
# download source code
git clone https://github.com/akk29/career-finder

# go inside directory
cd career-finder

# install, create virtualenv and activate virtualenv (optional)
python -m venv .venv
.venv\Scripts\activate # windows
.venv/Scripts/activate # linux

# install requirements
pip install -r requirements.txt

# run development server locally
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 2. Steps for runing project via docker

Pull publicly hosted image from docker repository & run directly on your system

```
docker run -d -p 8000:8000 --name careerfinder akk29/public:careerfinder
```

Visit : http://127.0.0.1:8000 in your browser
