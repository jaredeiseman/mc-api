# Mamas Connect API

## Setup Instructions For Local Environment
* Clone the repo
* Make sure Python 3.6+ and virtualenv/virtualenvwrapper are installed
* make a new virtualenv
* From the directory that houses manage.py and requirements.txt, run 'pip install -r requirements.txt'
* Install Postrgresql with brew: 'brew install postgresql'
  * If you want postgres to start with your machine run "brew services start postgresql"
* Create the dev user:
  * run 'psql postgres'
  * run "CREATE ROLE mcadmin WITH LOGIN PASSWORD 'mcadminpassword';"
  * ctrl + d to exit
* Run './manage.py makemigrations'
* Run './manage.py migrate'
* Run './manage.py createsuperuser' and follow the prompts
* Run './manage.py runserver' to start the server

The / route will land you in Swagger, the browsable API.

The /admin route will also give you access to add data to the Test Model, as well as manage users.
