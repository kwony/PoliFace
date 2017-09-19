from django.conf.urls import url
from .views import rank, resemble, info, home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home$', home, name='home'),
    url(r'^rank$', rank, name='rank'),
    url(r'^info$', info, name='info'),
    url(r'^resemble$', resemble, name='resemble'),
]