from django.urls import path
from . import views
urlpatterns=[
    path('student/',views.StudentApi.as_view()),
    path('student/<int:pk>',views.StudentApi.as_view()),
    ]