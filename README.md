Run the project:  python manage.py runserver_plus --cert-file cert.pem --key-file key.pem   
Run celery: celery -A cybersport worker --loglevel=info --pool=threads
Run rabbitmq-server: sudo service rabbitmq-server start
Enable rabbitmq_management: sudo rabbitmq-plugins enable rabbitmq_management
Rabbitmq_management: http://localhost:15672/