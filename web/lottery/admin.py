from django.contrib import admin

# Register your models here.
from lottery.models import LotteryUser

admin.site.register(LotteryUser)