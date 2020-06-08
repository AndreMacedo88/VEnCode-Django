web: gunicorn VEnCode_Django.wsgi --log-file -
worker: celery worker -A VEnCode_Django.celery --without-gossip --without-mingle --without-heartbeat --pool=solo
