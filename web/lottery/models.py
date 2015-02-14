from django.db import models

class LotteryUser(models.Model):
    username = models.CharField(max_length=16, primary_key=True)
    password = models.CharField(max_length=16)	
    phone = models.CharField(max_length=16)
    name = models.CharField(max_length=16)
    body_id = models.CharField(max_length = 32)
    address = models.CharField(max_length = 128)

    def __unicode__(self):
        return u'%s'%(self.username)

# Create your models here.
