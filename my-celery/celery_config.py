# -*- coding: utf-8 -*-
from celery.schedules import crontab
# from datetime import timedelta

'''定时任务'''
CELERY_TIMEZONE = CONFIG.TIMEZONE
CELERYBEAT_SCHEDULE = {
    'test': {
        'task': 'celery_task.hello',
        'schedule': crontab(hour=15, minute=00),
        'args': ("world")
    }
}
