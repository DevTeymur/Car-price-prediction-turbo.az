from os import name
from django.urls import path
from .views import ContactView
from .views import MainView, get_json_car_data, get_json_model_data

urlpatterns = [
    path('', MainView, name="main"),
    path('contact', ContactView.as_view(), name="contact"),
    path('cars-json/', get_json_car_data, name='cars-json'),
    path('models-json/<str:car>/', get_json_model_data, name='models-json'),
]