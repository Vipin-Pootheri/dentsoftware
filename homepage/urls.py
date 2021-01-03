from django.urls import path
from . import views
from django.urls import path


urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('adminhomepage/', views.adminhomepage, name='adminhomepage'),
    path('doctorhomepage/', views.doctorhomepage, name='doctorhomepage'),
    path('searchpatient/', views.searchpatient, name='searchpatient'),
    path('setpatient/', views.setpatient, name='setpatient'),
    path('checkinwalkin/', views.checkinwalkin, name='checkinwalkin'),




]
