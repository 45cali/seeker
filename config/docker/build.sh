curl https://raw.githubusercontent.com/45cali/seeker/master/config/docker/Dockerfile > ./Dockerfile

sudo docker build -t='seeker:mysqlv1' .

sudo docker run -d -i -t -P seeker:mysqlv1 /usr/sbin/apache2ctl -D FOREGROUND

