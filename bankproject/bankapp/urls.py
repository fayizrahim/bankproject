from . import views
from django.urls import path
from django. contrib import admin
urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register,name="register"),
    path('login',views.loginn,name='login'),
    path('logout',views.logout,name='logout'),
    path('newpage', views.newpage, name='newpage'),

    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
