from api import views
from django.urls import path
 
urlpatterns=[
path('stulist/', views.stu_list),
path('create/', views.stu_create),
path('update/', views.stu_update),
path('delete/', views.stu_delete)
]