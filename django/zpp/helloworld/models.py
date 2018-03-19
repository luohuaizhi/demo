import re
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

UNAME_REG = re.compile(r"^\w*")
DATE_REG = re.compile(r"(19\d{2})|(20\d{2})-(0[1-9])|(1[1-2])-(0[1-9])|([12][0~9])|(3[0-1])")

class User(models.Model):
    name = models.CharField(max_length=32)
    birthday = models.DateField()
    gender = models.BooleanField(default=True)
    desc = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)


logger = logging.getLogger(__name__)
 
@receiver(pre_save, sender=User)
def pre_save_handler(sender, **kwargs):
    
    # 我们可以在User这个Model保存之前尽情调戏了：）
    logger.debug("{},{}".format(sender, **kwargs))
    if not re.match(UNAME_REG, kwargs.uname):
        return 
    if not re.match(UNAME_REG, kwargs.udate):
        return 
