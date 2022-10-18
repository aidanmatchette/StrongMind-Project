# Strong Mind Assessment

### Live Application https://pizza.aidanmatchette.com/

## Setup

### Dependecies
- Python3
- PostgreSQL


### Clone repo (take note of ending dot if you don't want to make another subfolder)
~~~
git clone https://github.com/aidanmatchette/StrongMind-Project.git .
~~~

~~~
python3 -m venv .venv
~~~

#### (Windows) Go into virtual environment
~~~
.venv/scripts/activate.ps1
~~~

#### (Mac/Linux) Go into virtual environment
~~~
source venv/bin/activate
~~~

### Create a PostgreSQL database
~~~
createdb strongmind
~~~

### Install application dependencies
~~~.ve
pip install -r requirements.txt
~~~

### Load fixture data
~~~
python3 manage.py loaddata db
~~~

### Migrate to database
~~~
python manage.py migrate
~~~

### Run Tests
~~~
python manage.py test
~~~

### Run application 
~~~
python manage.py runserver
~~~

### Navigate to http://localhost:8000/
