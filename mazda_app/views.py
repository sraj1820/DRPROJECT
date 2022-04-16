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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'drcarcollector'
from .models import Car, Users, Mazda, Photo

# Create your views here.

class HomeListView(ListView):
     model = Car
     template_name = 'home.html'

class CarCreate(LoginRequiredMixin, CreateView):
     model = Car
     fields = ['name', 'make', 'car_model', 'year', 'mileage', 'color', 'new','company','users']
     success_url = ('/cars/')
     template_name = 'mazda_app/car_form.html'


     

class CarListView(LoginRequiredMixin,ListView):
     model = Car
     serializer_class = carSerializer
     template_name = 'car_list.html'

@login_required
def car_delete(request, car_id):
     car = Car.objects.get(id=car_id)
     car.delete()
     return redirect('/cars/')


class CarUpdate(LoginRequiredMixin,UpdateView):
     model = Car
     fields =['year', 'mileage', 'color', 'new']
     success_url = ('/cars/')

class MyCarsView(LoginRequiredMixin, ListView):
     model = Car
     template_name = 'my_cars.html'


@login_required
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


# def assoc_user(request, car_id, users_id):
#      # liked_cars_list = list()
#      # liked_cars = tuple(liked_cars_list)
     
#      liked_car= Car.objects.get(id=car_id).users.add(users_id)
#      # liked_cars = list(liked_cars)
#      # liked_cars.append(liked_car)
#      # liked_cars= tuple(liked_cars)
#      # print(liked_cars)
#      return render(request, 'my_cars.html', {liked_cars:liked_cars})

@login_required
def add_photo(request, car_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, car_id=car_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', car_id=car_id)

