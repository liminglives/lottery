# -*- coding: utf-8 -*-

import time


def checkCookies(request):
    if "username" not in request.COOKIES:
        print "username is not in cookies"
        return False
    return True

def checkAdminCookies(request):
    if "username" not in request.COOKIES:
        print "username is not in cookies"
        return False
    return True

def getCurRoundID():
    return '20150216';

def genOrderID():
    return '4323121'

def getCurTime():
    return time.strftime("%Y-%m-%d %H:%M")

def timeStampToTime(timestamp):
    print timestamp
    print type(timestamp)
    loc = time.localtime(float(timestamp))
    return time.strftime("%Y-%m-%d %H:%M", loc)

def transStatus(status):
    if status == 'open':
        return "未开奖"
    elif status == 'closed':
        return "已开奖"
    else:
        return "未定义"