from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView
from mazda_app.models import Car
from .serializers import carSerializer

# Create your views here.

class HomeListView(ListView):
     model = Car
     template_name = 'home.html'

class CarListView(ListView):
     model = Car
     serializer_class = carSerializer
     template_name = 'car_list.html'

def car_detail(request, car_id):
          car = Car.objects.get(id=car_id)
          return render(request,'detail.html')