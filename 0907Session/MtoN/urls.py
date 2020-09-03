"""MtoN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import blog.views
import movie.views

from django.conf import settings
from django.conf.urls.static import static
from MtoN.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/',UserCreateDoneTV.as_view(), name ='register_done'),
    path('', blog.views.home, name = "home"),

    path('blog/',include('blog.urls')),
    path('movie/',movie.views.movie, name="movie"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''