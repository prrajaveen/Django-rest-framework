from django.urls.resolvers import URLPattern
from . import views
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from api import views
router=routers.DefaultRouter()
router.register('student',views.StudentApi)


urlpatterns=[
    path('',include(router.urls))
]