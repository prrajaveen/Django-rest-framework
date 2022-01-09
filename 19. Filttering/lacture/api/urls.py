from django.urls import path
from api import views

urlpatterns=[
    path('studentapi/',views.StudentList.as_view())
]