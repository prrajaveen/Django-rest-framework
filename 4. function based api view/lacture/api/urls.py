from api import views
from django.urls import path
 
urlpatterns=[
path('stulist/', views.hello_world),
path('create/', views.stu_create),
# path('update/', views.stu_update),
# path('delete/', views.stu_delete)
]

# {
#     "name":"praveen kumar",
#     "roll":101,
#     "city":"muz"
# }