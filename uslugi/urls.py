from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.uslugi, name='uslugi'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.uslugi, name='info'),
]