from django.urls.conf import include
from api.models import Student
from django.db import router
from api.views import StudentApi
from django.urls import path
from api import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from api.auth import CustomAuthToken

router=routers.DefaultRouter()
router.register('student',views.StudentApi,basename='student')

urlpatterns=[
    path('',include(router.urls)),
    path('gettoken/',CustomAuthToken.as_view())
]