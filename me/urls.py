from django.contrib import admin
from django.urls import path
from me import views

urlpatterns = [

    path("",views.index, name='me'),   
    path("about/",views.about, name='about'),
    path("project/",views.project, name='project'),
    path("services/",views.services, name='services'),
    path("contact/",views.contact, name='contact'),
]
