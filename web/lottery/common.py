# -*- coding: utf-8 -*-

import time
import json

def checkCookies(request):
    if "username" not in request.COOKIES:
        print "username is not in cookies"
        return False
    return True

def checkAdminCookies(request):
    if "adminusername" not in request.COOKIES:
        print "username is not in cookies"
        return False
    return True

def getCurRoundID():
    return '20150216';

def genOrderID(roundID):
    random_time = str(int(time.time()*100))
    return roundID[2:] + random_time[6:]

def getCurTime():
    return time.strftime("%Y-%m-%d %H:%M")

def timeStampToTime(timestamp):
    print timestamp
    print type(timestamp)
    loc = time.localtime(float(timestamp))
    return time.strftime("%Y-%m-%d %H:%M", loc)

def mergeBuyData(sumData, buyData):
    sumorder = json.loads(sumData)
    buyorder = json.loads(buyData)

    print "sumdata", sumData
    print "buydata", buyData

    for key in buyorder:
        if not sumorder.has_key(key):
            sumorder[key] = buyorder[key]
            continue
        for key1 in buyorder[key]:
            if not sumorder[key].has_key(key1):
                sumorder[key][key1] = buyorder[key][key1]
                continue
            sumorder[key][key1] = int(sumorder[key][key1]) + int(buyorder[key][key1])
    
    print json.dumps(sumorder)

    return json.dumps(sumorder)

def transStatus(status):
    if status == 'open':
        return "未开奖"
    elif status == 'closed':
        return "已开奖"
    else:
        return "未定义"