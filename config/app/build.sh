#!/bin/bash
echo '################### SEEKER WITH MYSQL BUILD ###############################'
echo 'installing system dependencies'
apt-get update
apt-apt-get install -y python python-dev python-distribute python-pip
apt-get install -y git
apt-get install -y apache2 libapache2-mod-wsgi

easy_install -U pip

echo 'building seeker in /app dir'
mkdir /app
cd /app
git clone https://github.com/45cali/seeker.git
cd /app/seeker/
git checkout mysql

echo 'installing django dependencies via pip'
pip install -r requirements.txt

echo 'updating apache vhost conf'

cp /app/seeker/config/apache/seeker.conf /etc/apache2/sites-available/

a2dissite 000-default-conf
a2ensite seeker.conf

service apache2 reload

cd /app/seeker/
echo 'build db'
pwd
python manage.py makemigrations
python manage.py migrate
python manage.py syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('vagrant', 'admin@example.com', 'vagrant')" | python manage.py shell


service apache2 restart
