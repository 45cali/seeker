curl https://raw.githubusercontent.com/45cali/seeker/master/config/docker/Dockerfile > ./Dockerfile

sudo docker build -t='seeker:latest' .

sudo docker run -d -i -t -P seeker:latest /usr/sbin/apache2ctl -D FOREGROUND

