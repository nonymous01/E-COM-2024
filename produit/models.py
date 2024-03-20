from django.db import models
from datetime import date, datetime
# Create your models here.


class User(models.Model):
    username= models.CharField(max_length=200, blank=False)
    first_name=models.CharField(max_length=100,blank=False )
    last_name= models.CharField(max_length=100, blank=False)
    email= models.EmailField(default="email@email.com",unique=True)
    password= models.CharField(max_length=200, blank=False)
    date_creation= models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.username
class Produit(models.Model):
    name_pronduit= models.CharField(max_length=200, blank=False)
    prix= models.DecimalField(max_digits=100,decimal_places=2)
    description= models.TextField(max_length=1000)
    image= models.ImageField(upload_to='images/')
    date= models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name_pronduit