from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomeListView.as_view(), name='home'),
    path('cars/', views.CarListView.as_view(), name='all_cars'),
    path('cars/mycars', views.MyCarsView.as_view(), name='my_cars'),
    path('cars/<int:car_id>/', views.car_detail, name='detail'),
    path('cars/<int:car_id>/delete/', views.car_delete, name='car_delete'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cars/<int:car_id>/assoc_user/<int:users_id/', views.assoc_user, name='assoc_user')    


]