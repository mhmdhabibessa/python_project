from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('login',views.login),
    path('teacher',views.teacher),
    path('sp_teacher',views.sp_teacher),
]


