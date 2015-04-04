# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from lottery.models import LotteryUser, AdminUser, Order, Round, BaseInfo, SumOrder

admin.site.register(LotteryUser)
admin.site.register(AdminUser)
admin.site.register(Order)
admin.site.register(Round)
admin.site.register(BaseInfo)
admin.site.register(SumOrder)