# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from lottery import views, adminViews


urlpatterns = patterns('',
    url(r'^hello/$', views.hello, name='hello'),
    
    url(r'^$',views.redirectLogin,name='home'),

    #login
    url(r'^login/$', views.login, name='login'),
    url(r'^login/auth/$', views.loginAuth, name='loginAuth'),


    #buy
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^buy/success/$', views.buy_success, name='buy_success'),
    url(r'^buy/submit/$', views.buy_submit, name='buy_submit'),
    
    #order
    url(r'^order/$', views.getOrder, name='getOrder'),
    url(r'^order/detail/$', views.getOrderDetail, name='getOrderDetail'),


    # admin 
    url(r'^admin/order/$', adminViews.getOrder, name='getOrderAdmin'),
    url(r'^admin/login/$', adminViews.login, name='loginAdmin'),
    url(r'^admin/login/auth/$', adminViews.loginAuth, name='loginAuthAdmin'),
    url(r'^admin/home/$', adminViews.home, name="homeAdmin"),
    url(r'^admin/$', adminViews.redirectLogin, name='loginAdmin'),

    # admin round
    url(r'^admin/round/$', adminViews.getRound, name="roundAdmin"),
    url(r'^admin/round/create/$', adminViews.createRound, name="createRoundAdmin"),
    url(r'^admin/round/create/submit/$', adminViews.submitRound, name="submitRoundAdmin"),
    url(r'^admin/round/submit/$', adminViews.submitRound, name="submitRoundAdmin"),
    url(r'^admin/round/detail/$', adminViews.getRoundDetail, name="getRoundDetailAdmin"),


)