from pyexpat import model
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from mazda_app.models import Car
from .serializers import carSerializer
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class HomeListView(ListView):
     model = Car
     template_name = 'home.html'

class CarListView(ListView):
     model = Car
     serializer_class = carSerializer
     template_name = 'car_list.html'


def car_delete(request, car_id):
     car = Car.objects.get(id=car_id)
     car.delete()
     return redirect('/cars/')


class CarUpdate(UpdateView):
     model = Car
     fields =['year', 'mileage', 'color', 'new']
     success_url = ('/cars/')



def car_detail(request, car_id):
          car = Car.objects.get(id=car_id)
          return render(request,'detail.html',{'car':car})


def signup(request):
     error_message = ''
     if request.method == 'POST':
          form = UserCreationForm(request.POST)
          if form.is_valid():
               user= form.save()
               login(request,user)
               return redirect('/accounts/login/')
          else:
               error_message = 'invalid sign up, please try again'
     form = UserCreationForm()
     context = {'form': form, 'error_message': error_message}
     return render(request, 'registration/signup.html', context)
