from django.urls import path
from django.contrib import admin
from portapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('projects/',views.projects,name='projects'),
    path('linkedin/', views.linkedin, name='linkedin'),
    path('github/', views.github, name='github'),
    path('naukri/', views.naukri, name='naukri'),


]
