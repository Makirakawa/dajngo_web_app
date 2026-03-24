from django.urls import path
from . import views

urlpatterns = [
    path('window_two/',views. window_two),
    path('window_three/', views.window_three),
]
