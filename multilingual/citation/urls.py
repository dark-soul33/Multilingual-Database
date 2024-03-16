from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('sindhi/',views.Sindhi, name="sindhi"),
    path('northeast/',views.Northeast, name="northeast"),
    path('malayalam/',views.Malayalam, name="malayalam"),
    path('sindhi/<int:id>',views.sindhidesc, name="sindhidesc"),
    path('northeast/<int:id>',views.northeastdesc, name="northeastdesc"),
    path('malayalam/<int:id>',views.malayalamdesc, name="malayalamdesc")
]