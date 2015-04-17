curl https://raw.githubusercontent.com/45cali/seeker/mysql/config/docker/Dockerfile > ./Dockerfile

sudo docker build -t='seeker:1.0' .

sudo docker run -d -i -t -P seeker:1.0 /usr/sbin/apache2ctl -D FOREGROUND

