from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^$', views.upload),
    url(r'^test/$', views.test),
    url(r'^result/$', views.result),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
]
