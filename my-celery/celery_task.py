# -*- coding: utf-8 -*-
from celery import Celery

celery = Celery('my_task')
celery.config_from_object('celery_config')


@celery.task
def hello(to="123"):
	print "hello %s" % to