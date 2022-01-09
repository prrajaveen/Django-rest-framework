from django.urls import path
from . import views
urlpatterns=[
    path('get/',views.StudentList.as_view()),
    path('post/',views.StudentCreate.as_view()),
    path('get/<int:pk>/',views.StudentRetrive.as_view()),
    path('put/<int:pk>/',views.StudentUpdate.as_view()),
    path('delete/<int:pk>/',views.StudentDelete.as_view())
    ]