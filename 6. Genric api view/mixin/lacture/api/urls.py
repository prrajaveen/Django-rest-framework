from django.urls import path
from . import views
urlpatterns=[
    # path('student/',views.StudentList.as_view()),
    # path('student/',views.StudentCreate.as_view()),
    # path('student/<int:pk>/',views.StudentRetrive.as_view()),
    # path('student/<int:pk>/',views.StudentUpdate.as_view()),
    path('student/<int:pk>/',views.StudentDestroy.as_view())
    
    ]