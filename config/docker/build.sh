curl https://raw.githubusercontent.com/45cali/seeker/master/config/docker/Dockerfile > ./Dockerfile

sudo docker build -t='seeker:latest' .

sudo docker run -i -t='seeker:latest' -p 80:80 /usr/sbin/apache2 -D FOREGROUND