from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomeListView.as_view(), name='home'),
    path('cars/', views.CarListView.as_view(), name='allcars'),
    path('cars/<int:car_id>/', views.car_detail, name='detail'),
]