# Career Finder

### 1. Steps for setting project locally - via source code (Will take time)

```
# download source code
git clone https://github.com/babygame0ver/Career-Finder

# go inside directory
cd Career-Finder

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

### 2. Steps for runing project locally - via Docker image (Easy & preferred - no dependencies installation)

Pull publicly hosted image from docker repository & run directly on your system

```
docker run -d -p 8000:8000 --name careerfinder babygame0ver/docker-repository:careerfinder
```

Visit : http://127.0.0.1:8000 in your browser
