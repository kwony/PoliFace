from django.conf.urls import url
from .views import rank, resemble, info, info_detail, info_upload_politician_list, home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^home$', home, name='home'),
    url(r'^rank$', rank, name='rank'),
    url(r'^info$', info, name='info'),
    url(r'^info/(?P<pk>\d+)/$', info_detail, name='info_detail'),
    url(r'^info_upload_politician_list$', info_upload_politician_list, name='info_upload_politician_list'),
    url(r'^resemble$', resemble, name='resemble'),
]