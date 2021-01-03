from . import views
from django.urls import path


urlpatterns = [

    path('newpatient/', views.newpatient, name='newpatient'),
    path('newpatient/createnewpatient/', views.createnewpatient, name='createnewpatient'),
    path('newpatient/getstate/', views.getstate, name='getstate'),

    path('appointment/', views.appointment, name='appointment'),
    path('appointment/draganddrop/', views.draganddrop, name='draganddrop'),
    path('appointment/checkin', views.checkin, name='checkin'),
    path('appointment/delete', views.delete, name='delete'),
    path('appointment/update', views.update, name='update'),
    path('appointment/registerafterappointment', views.registerafterappointment, name='registerafterappointment'),






]