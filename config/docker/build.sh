git clone https://github.com/45cali/seeker.git

cd seeker/

git checkout mysql

cd ../

cp seeker/config/docker/Dockerfile ./

sudo docker build -t='seeker:1.0' .

sudo docker run -d -i -t seeker:1.0 

