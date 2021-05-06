Uruchomienie Aplikacji:
cd ścieżka folderu aplikacji
set FLASK_APP=run.py
set FLASK_ENV=development
python -m flask run


Czyszczenie bazy:
python 
from tracker import db
db.drop_all()

Jeżeli baza nie jest utworzona bądź pusta:
python 
from tracker import db
db.create_all()