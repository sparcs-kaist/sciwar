sciwar
======

Science-war homepage project for 2013 Postech-KAIST Science-war event

http://science-war.kaist.ac.kr

Running
-------

```sh
virtualenv --distribute env
source env/bin/activate
pip install -r requirements.txt
python manage.py syncdb
python manage.py loaddata schedule.json
python manage.py loaddata player.json
python manage.py loaddata player2.json
python manage.py runserver
```
