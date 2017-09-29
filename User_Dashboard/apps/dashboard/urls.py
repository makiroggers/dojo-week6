# FOR APPS
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.user_dashboard, name='user_dashboard'),
    url(r'^$', views.admin_dashboard, name='admin_dashboard'),
]

