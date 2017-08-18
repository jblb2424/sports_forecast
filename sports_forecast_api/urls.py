"""tutory_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

v1_urls = [
    url(r'^', include('common.v1.urls')),
]

api_urls = [
    # url(r'^auth/', include('knox.urls')),
    # url(r'^auth/', include('rest_auth.urls')),
    # url(r'^auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^allauth/', include('allauth.urls')),
    url(r'^drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/', include(v1_urls, namespace='v1')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
