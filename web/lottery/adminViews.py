# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.template import RequestContext, loader

from django.views.decorators.csrf import csrf_exempt

from lottery.models import *

import common
import json

def getOrder(request):
    print "enter admin getOrder"
    if not common.checkAdminCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/admin/login/')

    return render_to_response("admin_user/order.html")

def login(request):
    print "enter admin login"
    return render_to_response("admin_user/login.html")

def redirectLogin(request):
    return HttpResponseRedirect("/lottery/admin/login/")

def home(request):
    print "enter admin home"
    if not common.checkAdminCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/admin/login/')

    return render_to_response("admin_user/home.html")

def getRound(request):
    print "enter admin getRound"
    if not common.checkAdminCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/admin/login/')

    round_list = Round.objects.values('round_id', 'round_th', 'pingma', 'tema', 'status').order_by('-round_id')

    print round_list
    return render_to_response('admin_user/round.html', {'round_list':round_list})

def createRound(request):
    print "enter admin create round"
    if not common.checkAdminCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/admin/login/')

    return render_to_response("admin_user/create_round.html")

def getRoundDetail(request):
    print "enter admin get round detail"
    if not common.checkAdminCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/admin/login/')
    data = None
    try:
        roundDtail = Round.objects.values('round_id', 'round_th', 'open_time', 'colse_time', \
            'result_time', 'status', 'pingma', 'tema').filter(round_id=request.GET['round_id'])[0]
        data = json.dumps(roundDtail)
        print data
    except Exception, e:
        print e
        print 'admin getRoundDetail error'

    return HttpResponse(data)

@csrf_exempt
def updateRound(request):
    print 'enter admin update round'
    if not common.checkAdminCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/admin/login/')
    
    print request.POST
    status = "open"

    if len(request.POST['pingma']) > 0:
        status = 'closed'
    try:
        roundItem = Round.objects.get(round_id=request.GET['round_id'])
        
        roundItem.round_th = int(request.POST['roundth'])
        roundItem.open_time = request.POST['opentime']
        roundItem.colse_time = request.POST['closedtime']
        roundItem.result_time = request.POST['resulttime']
        roundItem.status = status
        roundItem.pingma = request.POST['pingma']
        roundItem.tema = request.POST['tema']
        
        #roundItem.update(round_th=int(request.POST['roundth']), open_time=request.POST['opentime'],\
        #    colse_time=request.POST['closedtime'], result_time=request.POST['resulttime'], status=status,\
        #    pingma=request.POST['pingma'], tema=request.POST['tema'])
        roundItem.save()
    except Exception, e:
        print 'update round error'
        print e

    return HttpResponseRedirect('/lottery/admin/round/')    

@csrf_exempt
def submitRound(request):
    print "enter admin create round"
    if not common.checkAdminCookies(request):
        print "cookies error"
        return HttpResponseRedirect('/lottery/admin/login/')
    
    print request.POST
    roundID = request.POST['resulttime'][0:4]
    roundth = request.POST['roundth']
    roundID = roundID + roundth
    isExist = False

    try:
        Round.objects.get(round_id = roundID)
        isExist = True
    except:
        isExist = False

    if isExist:
        errorTitle = "新 建 一 期 失 败！"
        errorContent = "期数已存在，请重新输入期数"
        return render_to_response("admin_user/error.html", {'error_title':errorTitle, 'error_content':errorContent})

    try:
        newRound = Round(round_id=roundID, round_th=int(roundth), open_time=request.POST['opentime'],
            colse_time=request.POST['closedtime'], result_time=request.POST['resulttime'], status='open', pingma='',tema='')
        newRound.save()
    except Exception, e:
        print "submit Round error"
        print e
        errorTitle = "新 建 一 期 失 败！"
        errorContent = "请重新创建"
        return render_to_response("admin_user/error.html", {'error_title':errorTitle, 'error_content':errorContent})

    return HttpResponseRedirect('/lottery/admin/round/')


@csrf_exempt
def loginAuth(request):
    print "enter admin login auth"

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
        user = AdminUser.objects.filter(username__exact = request.POST["username"], password__exact = request.POST["password"])
    except Exception, e:
        print e
    if user:
        response = HttpResponse()
        response.set_cookie('username',request.POST["username"])

        return response
    else:
        return HttpResponseNotFound("404")

