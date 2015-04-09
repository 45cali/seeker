#!/bin/bash

echo 'installing system dependencies'
apt-get update
apt-get install -y git
apt-get install -y apache2 libapache2-mod-wsgi
apt-get install -y python-pip

echo 'building seeker in /app dir'
mkdir /app
cd /app
git clone https://github.com/45cali/seeker.git
cd /app/seeker/
echo 'installing django dependencies via pip'
pip install -r requirements.txt

echo 'updating apache vhost conf'

cp /app/seeker/config/apache/seeker.conf /etc/apache2/sites-available/

a2dissite 000-default-conf
a2ensite seeker.conf

service apache2 reload

cd /app/seeker/
echo 'build db'
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('vagrant', 'admin@example.com', 'vagrant')" | python manage.py shell

cd /

chown www-data:www:data /app/seeker/
chown www-data:www-data /app/seeker/db*

service apache2 restart
