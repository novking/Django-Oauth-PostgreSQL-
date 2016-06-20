from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^todo/create/$', views.todo, name="create"),
    url(r'^todo/$', views.display, name="list"),
    url(r'^todo/(?P<id>\d+)/delete/$', views.delete, name="delete")

]
