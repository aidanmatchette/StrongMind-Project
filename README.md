# Strong Mind Assessment


## Setup



### Clone repo (take note of ending dot if you don't want to make another subfolder)
~~~
git clone https://github.com/aidanmatchette/StrongMind-Project.git .
~~~

~~~
python -m venv .venv
~~~

#### (Windows) Go into virtual environment
~~~
.venv/scripts/activate.ps1
~~~

#### (Mac/Linux) Go into virtual environment
~~~
source venv/bin/activate
~~~

~~~.ve
pip install -r requirements.txt
~~~

~~~
python manage.py migrate
~~~

~~~
python manage.py runserver
~~~

