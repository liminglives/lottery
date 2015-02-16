# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseForbidden
from django.template import RequestContext, loader

from django.views.decorators.csrf import csrf_exempt

from lottery.models import *

import common

# Create your views here.

def hello(request):
	return render_to_response('client/hello_.html') #HttpResponse("hello world")

def login(request):
	return render_to_response('client/login.html')

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

	return render_to_response('client/buy.html');

def buy_success(request):
	return render_to_response('client/success_buy.html')

@csrf_exempt
def buy_submit(request):
	print 'enter buy_submit'
	if request.method != 'POST':
		print 'http method is not post'
		return HttpResponseForbidden()

	if not common.checkCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/login/')

    #check the deadline

    username = request.COOKIES["username"]
    newOrder = Order(order_id=common.genOrderID(), round_id=common.getCurRoundID(),
    	data=request.POST['databuy'], windata="", 
    	buy_amount=int(request.COOKIES['sumbuy']), win_amount=0, net_amount=0,
    	status='open', username=username)

    newOrder.save()

	print request.POST
	return HttpResponse("提交成功")

def getOrder(request):
	print 'enter getOrder'
	return render_to_response('client/order.html')
