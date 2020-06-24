# Flask App Boilerplate

Quick start for Flask apps.

Pre-reqs: Virtualenv

To use:
    
-> Open your terminal

-> Navigate to the `flask_app_boilerplate` dir

-> Set up a virtualenv environment: ` $ virtualenv env `

-> Activate virtual environment: ` $ source env/bin/activate `

-> Install dependencies: ` $ pip install flask flask-sqlalchemy flask-migrate flask-wtf 
flask-script gunicorn python-dotenv `

-> Set .env variables. FLASK_ENV, FLASK_APP, DATABASE_URL have default settings. You will 
need to set the secret key, host, and port.

-> Configure .gitignore

-> Initialize DB: ` $ flask db init `

-> Create your models in models.py

-> To make migrations: ` $ flask db migrate `

-> To apply migrations: ` $ flask db upgrade `
