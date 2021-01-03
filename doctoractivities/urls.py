from django.urls import path
from . import views

urlpatterns = [


    path('alert/', views.alerts, name='alerts'),
    path('prescription/', views.prescription, name='prescription'),
    path('radiologyimages/', views.radiologyimages, name='radiologyimages'),
    path('dentalchart/', views.dentalchart, name='dentalchart'),
    path('dentalchart/savetreatment', views.savetreatment, name='savetreatment'),
    path('dentalchart/saveeditedtreatment', views.saveeditedtreatment, name='saveeditedtreatment'),
    path('dentalchart/getfee', views.getfee, name='getfee'),
    path('billing/', views.billing, name='billing'),
    path('checkout/', views.checkout, name='checkout'),




]
