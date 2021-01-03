from django.urls import path
from . import views

urlpatterns = [

    path('', views.loginpage, name='loginpage'),
    path('logout/', views.logout_view, name='logout'),
]
