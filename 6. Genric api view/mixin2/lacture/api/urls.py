from django.urls import path
from . import views
urlpatterns=[
    path('student/',views.StudentList.as_view()),
    path('student/<int:pk>/',views.StudentRetrive.as_view())
    
    ]