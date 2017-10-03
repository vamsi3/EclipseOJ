from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^(?P<username>[a-zA-Z0-9_@.+-]+)/$', views.userspecific, name='userspecific'),
]
