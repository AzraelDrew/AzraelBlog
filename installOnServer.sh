sudo apt install python3 nginx uwsgi libpython3.8-dev python3-venv;
python3 -m venv /var/www/venv $$ source /var/www/venv/bin/activate;
pip3 install django django-simpleui djangorestframework django-cors-headers Pillow requests beautifulsoup4;