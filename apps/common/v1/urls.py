from django.conf.urls import url

from . import views

urlpatterns = [
url(r'^detail/(?P<pk>\d+)', views.detail),
url(r'^$', views.index),
]
