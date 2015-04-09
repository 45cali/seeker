#!/bin/bash

echo 'installing system dependencies'
apt-get update
apt-get install -y git
apt-get install -y apache libapache2-mod-wsgi
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
service apache2 restart