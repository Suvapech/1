from django.contrib import admin
from django.urls import path
from modelFormsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ListProjects/', views.list_projects, name='list_projects'),
    path('AddProject/', views.add_project, name='add_project'),
    path('UserRegistration/', views.user_registration, name='user_registration'),
    path('AppProject/', views.app_project, name='app_project'),
    path('hello/', views.hello, name='hello'),
]
