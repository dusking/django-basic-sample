
## About ##

This is the most basic sample of django, based on Django 1.9 tutorial.
In addition to the basic Django sample, it's also using nginx, Gunicorn and postgres.
It is based on the following tutorials.
Each of the following tutorials is a stand alone guide. reading them one after another can help you to understand the production architecture concept.

 * [Django basic sample](https://docs.djangoproject.com/en/1.9/intro/tutorial01/)
 * [Django and nginx](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
 * [django with postgres, nginx and gunicorn](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-14-04)
 * [complete architecture](https://github.com/rogueleaderr/definitive_guide_to_django_deployment)


## System Files ##

* In case you followed all the above tutorials, at the end you'll have the following system files:

 * /etc/rc.local file: (if you're using uwsgi with nginx, no need if using gunicorn with nginx)
```bash
/usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data

exit 0
```

 * /etc/init/gunicorn.conf file:
```bash
description "Gunicorn application server handling mysite"

start on runlevel [2345]
stop on runlevel [!2345]

respawn
setuid me
setgid www-data
chdir /home/me/srv/django-basic-sample/mysite

exec /home/me/.virtualenvs/dev/bin/gunicorn --workers 3 --bind unix:/home/me/srv/django-basic-sample/mysite/mysite.sock mysite.wsgi:application
```

* Run (should be autostart on restart)
```bash
sudo service gunicorn start
sudo service nginx start
```

## Running on your machine ##
When testing it locally, it's best using [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html).
