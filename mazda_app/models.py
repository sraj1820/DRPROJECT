from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    color = models.CharField(max_length=50)
    new = models.BooleanField(default = False)

    users = models.ManyToManyField(Users)
     
    def __str__(self):
        return self.name

class Mazda(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    reg_num = models.CharField(max_length=10)

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


