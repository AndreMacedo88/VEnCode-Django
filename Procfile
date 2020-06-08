web: gunicorn VEnCode_Django.wsgi --log-file -
worker: celery worker --app=VEnCode_Django.celery --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
