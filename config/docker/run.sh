#!/bin/bash

echo "from django.contrib.auth.models import User; User.objects.create_superuser('vagrant', 'admin@example.com', 'vagrant')" | python /app/seeker/manage.py shell

