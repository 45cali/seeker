curl https://raw.githubusercontent.com/45cali/seeker/mysql/config/docker/Dockerfile > ./Dockerfile

sudo docker build -t='seeker:mysql' .

sudo docker run -d -i -t -P seeker:mysql /usr/sbin/apache2ctl -D FOREGROUND

