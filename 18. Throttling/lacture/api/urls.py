from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView,TokenVerifyView


router=DefaultRouter()
router.register('studentapi',views.StudentApi,basename='student')

urlpatterns=[
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]