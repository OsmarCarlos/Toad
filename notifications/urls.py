# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import test

urlpatterns = [

    url(r'test/$', test),
]
