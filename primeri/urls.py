from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.raboti, name='primer_rabot'),
]