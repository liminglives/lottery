# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from lottery import views

urlpatterns = patterns('',
    url(r'^hello/$', views.hello, name='hello'),
    
    #login
    url(r'^login/$', views.login, name='login'),
    url(r'^login/auth/$', views.loginAuth, name='loginAuth'),


    #buy
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^buy/success/$', views.buy_success, name='buy_success'),
    url(r'^buy/submit/$', views.buy_submit, name='buy_submit'),
    
    #order
    url(r'^order/$', views.getOrder, name='getOrder'),

)