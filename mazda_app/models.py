
from django.db import models

# Create your models here.
class Mazda(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    reg_num = models.CharField(max_length=10)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'mazda'

# users
class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'user'

# cars
class Car(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    color = models.CharField(max_length=50)
    new = models.BooleanField(default = False)
    company = models.ForeignKey(Mazda, on_delete=models.CASCADE)
    users = models.ManyToManyField(Users)
    

     
    def __str__(self):
        return self.make
    class Meta:
        verbose_name_plural = 'car'

#photos 
class Photo(models.Model):
    url = models.CharField(max_length=200)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for car_id: {self.car_id} @{self.url}"




