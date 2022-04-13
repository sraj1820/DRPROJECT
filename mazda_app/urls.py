from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomeListView.as_view(), name='home'),
    path('cars/', views.CarListView.as_view(), name='allcars'),
    path('cars/<int:car_id>/', views.car_detail, name='detail'),
    path('cars/<int:car_id>/delete/', views.car_delete, name='car_delete'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('accounts/signup/', views.signup, name='signup'),


]