from django.urls import path
from . import views

urlpatterns = [

    path('user/', views.adduser, name='adminadduser'),
    path('user/edituser/', views.edituser, name='edituser'),
    path('deleteuser/<int:id>', views.deleteuser, name='deleteuser'),
    path('adminaddprescription/', views.addprescription, name='adminaddprescription'),
    path('adminaddtreatmentplan/', views.addtreatmentplan, name='adminaddtreatmentplan'),

]
