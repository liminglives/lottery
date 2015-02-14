from django.conf.urls import patterns, url

from lottery import views

urlpatterns = patterns('',
    url(r'^hello/$', views.hello, name='hello'),
)