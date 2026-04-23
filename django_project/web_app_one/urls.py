from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<int:about_cars>/', views.get_info_about_cars_by_number),
    path('<str:about_cars>/', views.get_info_about_cars, name='auto_list_name'),
    path('<int:about_moto>/', views.get_info_about_cars_by_number),
    path('<str:about_moto>/', views.get_info_about_cars, name='auto_list_name'),
]
