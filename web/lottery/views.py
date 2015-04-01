# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import RequestContext, loader

from django.views.decorators.csrf import csrf_exempt

from lottery.models import *

import common
import json

# Create your views here.

def hello(request):
    return render_to_response('client/hello_.html') #HttpResponse("hello world")

def login(request):
    return render_to_response('client/login.html')

def redirectLogin(request):
    return HttpResponseRedirect("/lottery/login/")

@csrf_exempt
def loginAuth(request):
    print "enter loginAuth"
    print request.POST
    if request.method != 'POST':
        print "http method is not post"
        return HttpResponseForbidden()

    #if not request.session.test_cookie_worked():
    #    return HttpResponseForbidden("Please open cookie")
    #request.session.delete_test.cookie()

    if "username" not in request.POST or "password" not in request.POST:
        print "request params error"
        return HttpResponseForbidden()
    user = None
    try:
        user = LotteryUser.objects.filter(username__exact = request.POST["username"], password__exact = request.POST["password"])
    except Exception, e:
        print e
    if user:
        response = HttpResponse()
        response.set_cookie('username',request.POST["username"])

        return response
    else:
        return HttpResponseNotFound("404")

def buy(request):
    print "enter buy"
    if not common.checkCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/login/')

    return render_to_response('client/buy.html');

def buy_success(request):
    return render_to_response('client/success_buy.html')

@csrf_exempt
def buy_submit(request):
    print 'enter buy_submit  tt'
    if request.method != 'POST':
        print 'http method is not post'
        return HttpResponseForbidden()

    if not common.checkCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/login/')

    #check the deadline
    try:
        username = request.COOKIES["username"]
        newOrder = Order(order_id=common.genOrderID(), round_id=Round.objects.get(round_id=common.getCurRoundID()),
            data=request.POST['databuy'], win_data="", buy_time=common.getCurTime(),
            buy_amount=int(request.POST['sumbuy']), win_amount=0, net_amount=0,
            status='open', username=LotteryUser.objects.get(username=username))

        print 'saving new order ... '
        print type(Round.objects.get(round_id=common.getCurRoundID()))
        newOrder.save()
    except Exception, e:
        print 'buy_submit causes exception'
        print e 
        return HttpResponseForbidden()

    print request.POST
    return HttpResponse("提交成功")

def getOrder(request):
    print 'enter getOrder'

    if not common.checkCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/login/')

    order_list = Order.objects.values('order_id', 'round_id', 'buy_amount', 'win_amount', \
        'buy_time', 'status').filter(username=request.COOKIES['username'])

    for item in order_list:
        #print type(item['round_id'])
        #print item['round_id']
        item['round_th'] = Round.objects.values('round_th').filter(round_id=item['round_id'])[0]['round_th']
        #item['buy_time'] = common.timeStampToTime(item['buy_time'])
        item['status'] = common.transStatus(item['status'])

    return render_to_response('client/order_list.html', {'order_list':order_list})

def getOrderDetail(request):
    print 'enter getOrderDetail'
    print request.GET

    if not common.checkCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/login/')
    orderData = None
    data = None
    try:
        orderData = Order.objects.values('round_id', 'buy_amount', 'win_amount',\
            'buy_time', 'status', 'data', 'win_data').filter(username=request.COOKIES['username'], order_id=request.GET['order_id'])[0]
        roundData = Round.objects.values('round_th', 'result_time', 'pingma', 'tema').filter(round_id=orderData['round_id'])[0]
        orderData['status_'] = common.transStatus(orderData['status'])
        roundData["result_time"] = common.timeStampToTime(roundData["result_time"])
        data = json.dumps({'orderData':orderData, 'roundData':roundData})
        print data
    except Exception, e:
        print e

    return HttpResponse(data)
