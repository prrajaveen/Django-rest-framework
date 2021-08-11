from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('studentapi',views.StudentApi,basename='student')

urlpatterns=[
    path('',include(router.urls))
]