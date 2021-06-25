from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('',Index,name='index'),
    path('signup/',signup,name='signup'),
    path("logout", logout, name="logout"),
    path("update/<int:pk>", UpdateTask.as_view(), name="update"),
    path("delete/<int:pk>", DeleteTask.as_view(), name="delete"),
    path("create/", CreateTask.as_view(), name="create")
]
