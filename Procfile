web: gunicorn app:app --log-file=-

init: python app.py db init
migrate: python app.py db migrate
upgrade: python app.py db upgrade