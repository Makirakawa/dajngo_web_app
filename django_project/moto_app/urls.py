from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:about_moto>/', views.get_info_about_moto_by_number),
    path('<str:about_moto>/', views.get_info_about_moto, name='moto_list_name'),
]