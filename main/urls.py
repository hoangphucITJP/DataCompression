from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^download/$', views.download, name='download'),
    url(r'^tracking', views.tracking, name='tracking'),
    url(r'^upload', views.upload, name='upload'),
]