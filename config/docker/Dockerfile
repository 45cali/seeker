FROM ubuntu:trusty

MAINTAINER Nicholas Colbert <nicholas.colbert@ticketmaster.com>

RUN apt-get update && apt-get -y install apache2 && apt-get clean

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# SSL SUPPORT
#RUN /bin/ln -sf ../sites-available/default-ssl /etc/apache2/sites-enabled/001-default-ssl
#RUN /bin/ln -sf ../mods-available/ssl.conf /etc/apache2/mods-enabled/
#RUN /bin/ln -sf ../mods-available/ssl.load /etc/apache2/mods-enabled/

RUN apt-get install -y libapache2-mod-wsgi libmysqlclient-dev && apt-get clean

RUN apt-get install -y python python-dev python-distribute python-pip  && apt-get clean

RUN mkdir -p /app/seeker/

COPY ./seeker/ /app/seeker/

RUN cp /app/seeker/config/apache/seeker.conf /etc/apache2/sites-available/

RUN a2dissite 000-default.conf

RUN a2ensite seeker.conf

RUN pip install -r /app/seeker/requirements.txt

EXPOSE 3306
EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

WORKDIR /app/seeker/

CMD ["python", "manage.py", "syncdb"]

