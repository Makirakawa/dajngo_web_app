from django.urls import path
from . import views

urlpatterns = [
    path('<int:about_cars>/', views.get_info_about_cars_by_number),
    path('<str:about_cars>/', views.get_info_about_cars),
]
