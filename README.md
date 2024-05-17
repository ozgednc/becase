## Prepare environment and db
1. Clone the repository.
2. Create virtual environment.
```
python -m virtualenv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```
3. Prepare db and create an admin user.
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
4. Run the application.
```
python manage.py runserver
```
Go to http://localhost:8000/applications/contact/ and fill the form. If you want to see the collected data you can use the admin panel (http://localhost:8000/admin).
