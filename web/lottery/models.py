# -*- coding: utf-8 -*-

from django.db import models

#should split this model
class LotteryUser(models.Model):
    username = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=128)
    pay_password = models.CharField(max_length=128) 
    phone = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    body_id = models.CharField(max_length = 32)
    address = models.CharField(max_length = 128)
    user_type = models.CharField(max_length = 16)
    email = models.EmailField(max_length = 254)
    create_date = models.CharField(max_length = 64)
    remark = models.TextField(null=True,blank=True)
    off_percent = models.IntegerField()
    #buy_sum = models.IntegerField()
    #win_sum = models.IntegerField()
    deposit = models.IntegerField()


    def __unicode__(self):
        return u'%s %s'%(self.username, self.name)

class AdminUser(models.Model):
    username = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=128)
    modify_password = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length = 254)

    def __unicode__(self):
        return u'%s %s'%(self.username, self.phone)


class Order(models.Model):
    order_id = models.CharField(max_length = 128, primary_key=True)
    #round_th = models.IntegerField()
    round_id = models.ForeignKey('Round', db_column='round_id')
    data = models.TextField() #buy_data
    win_data = models.TextField(null=True,blank=True)
    buy_amount = models.IntegerField() 
    win_amount = models.IntegerField()
    net_amount = models.IntegerField()
    buy_time = models.CharField(max_length=64)
    status = models.CharField(max_length=16)
    username = models.ForeignKey('LotteryUser')
    remark = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return u'%s %s %s %s'%(self.order_id, self.round_id, self.status, self.username)


class SumOrder(models.Model):
    round_id = models.ForeignKey('Round', db_column='round_id')
    data = models.TextField()
    win_data = models.TextField(null=True,blank=True)
    buyout_data = models.TextField(null=True,blank=True)
    buy_amount = models.IntegerField() 
    win_amount = models.IntegerField()
    net_amount = models.IntegerField()
    buyout_amount = models.IntegerField()
    sum_data = models.TextField(null=True,blank=True)



class Round(models.Model):
    round_id = models.CharField(max_length = 128, primary_key=True)
    round_th = models.IntegerField() #should be char
    open_time = models.CharField(max_length=64)
    colse_time = models.CharField(max_length=64) #closed_time
    result_time = models.CharField(max_length=64)

    pingma = models.CharField(max_length = 32)
    tema = models.CharField(max_length = 4)

    status = models.CharField(max_length=16) #open, stop, closed

    def __unicode__(self):
        return u'%s %s %s'%(self.round_id, self.round_th, self.open_time)

class BaseInfo(models.Model):
    zodiac_year = models.CharField(max_length = 16)
    deadline = models.CharField(max_length=64)
    tema_odds = models.IntegerField() #pei lv
    off_percent = models.IntegerField()
