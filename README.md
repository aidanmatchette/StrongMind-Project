# Strong Mind Assessment

### Live Application https://pizza.aidanmatchette.com/

## Setup

### Dependecies
- [Python3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)
- Python Venv
~~~
pip install virualenv
~~~

### Clone repo (take note of ending dot if you don't want to make another subfolder)
~~~
git clone https://github.com/aidanmatchette/StrongMind-Project.git
~~~
~~~
cd StrongMind-Project
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
source .venv/bin/activate
~~~

### [Create a PostgreSQL database](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)
~~~
createdb strongmind
~~~

### Install application dependencies
~~~.ve
pip install -r requirements.txt
~~~

### Run Tests
~~~
python manage.py test
~~~

### Migrate to database
~~~
python3 manage.py migrate
~~~

### Load fixture data
~~~
python3 manage.py loaddata db
~~~



### Run application 
~~~
python3 manage.py runserver
~~~

### Navigate to http://localhost:8000/
