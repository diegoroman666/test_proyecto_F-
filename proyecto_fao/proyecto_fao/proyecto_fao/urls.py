from django.urls import path

from fao_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
]