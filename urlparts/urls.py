from django.conf.urls import url
from . import views

app_name = 'urlparts'

urlpatterns = [
	url(r'^(?P<page_alias>.+?)/$', views.index),
]
