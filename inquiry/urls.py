from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^inquiry/list/$', views.inquiry_list, name='inquiry_list'),
    url(r'^inquiry/(?P<pk>\d+)/$', views.inquiry_detail, name='inquiry_detail'),
    url(r'^inquiry/new/$', views.inquiry_new, name='inquiry_new'),
    url(r'^inquiry/(?P<pk>\d+)/edit/$', views.inquiry_edit, name='inquiry_edit'),
    url(r'^inquiry/pending/$', views.inquiry_pending, name='inquiry_pending'),
    url(r'^inquiry/resolved/$', views.inquiry_resolved, name='inquiry_resolved'),
    url(r'^inquiry/tasks/$', views.inquiry_task, name='inquiry_task'),
]