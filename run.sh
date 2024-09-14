#!/bin/bash

python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput

echo "from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='Marco').exists():
    User.objects.create_superuser('Marco', 'fedemarkco@gmail.com', '1234')
" | python3 manage.py shell

python3 manage.py runserver 0.0.0.0:8000