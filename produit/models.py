from django.db import models
from datetime import date, datetime
from django.utils import timezone
from autoslug import AutoSlugField
# Create your models here.


class User(models.Model):
    username= models.CharField(max_length=200, blank=False)
    first_name=models.CharField(max_length=100,blank=False )
    last_name= models.CharField(max_length=100, blank=False)
    email= models.EmailField(default="email@email.com",unique=True)
    password= models.CharField(max_length=200, blank=False)
    date_creation= models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.username
class ProduitDeal(models.Model):
    name_produit= models.CharField(max_length=200, blank=False)
    slug= AutoSlugField(populate_from="name_produit", null=True)
    prix= models.DecimalField(max_digits=100,decimal_places=0)
    description= models.CharField(max_length=1000)
    detail= models.TextField(max_length=100000000,null=True, default="Disponible")
    image= models.ImageField(upload_to='media/produitimages/',null=True)
    image_detail_1= models.ImageField(upload_to='media/produitimages/',null=True)
    image_detail_2= models.ImageField(upload_to='media/produitimages/',null=True)
    off=models.DecimalField(max_digits=100,decimal_places=2)
    like=models.BooleanField(default=False)
    date_ajout = models.DateTimeField(default=timezone.now)
    choix = {
        "En stock": "En stock",
        "Disponible": "Disponible",
        "Indisponible": "Indisponible",
    }
    stock= models.CharField(max_length=20,choices=choix, default='Disponible')


    def __str__(self) -> str:
        return self.name_produit
    #afficher les elements en orde de creation
    class Meta:
        ordering=['-date_ajout']

    #géré les erreur lorqu'il ya pas d'image
    @property
    def ImageUrl(self):
        try:
            url= self.image.url
        except:
            url=''
        return url

class TopProducts(models.Model):
    name_produit= models.CharField(max_length=200, blank=False)
    prix= models.DecimalField(max_digits=100,decimal_places=0)
    slug= AutoSlugField(populate_from="name_produit", null=True)
    description= models.CharField(max_length=1000)
    detail= models.TextField(max_length=100000000,null=True)
    image= models.ImageField(upload_to='media/topimages/',null=True)
    image_detail_1= models.ImageField(upload_to='media/topimages/',null=True)
    image_detail_2= models.ImageField(upload_to='media/topimages/',null=True)
    off=models.DecimalField(max_digits=100,decimal_places=2)
    like=models.BooleanField(default=False)
    date_ajout = models.DateTimeField(default=timezone.now)
    choix = {
        "En stock": "En stock",
        "Disponible": "Disponible",
        "Indisponible": "Indisponible",
    }
    stock= models.CharField(max_length=200,choices=choix, default='Disponible')


    def __str__(self) -> str:
        return self.name_produit
    #afficher les elements en orde de creation
    class Meta:
        ordering=['-date_ajout']

    #géré les erreur lorqu'il ya pas d'image
    @property
    def ImageUrl(self):
        try:
            url= self.image.url
        except:
            url=''
        return url
    
class Grilles(models.Model):
    name_grille= models.CharField(max_length=200)
    images = models.ImageField(upload_to='media/Grille/', default='default_image.jpg')
    date_ajout = models.DateTimeField(default=timezone.now)
   
    def __str__(self) -> str:
        return self.name_grille
    #afficher les elements en orde de creation
    class Meta:
        ordering=['-date_ajout']

    #géré les erreur lorqu'il ya pas d'image
    @property
    def ImageUrl(self):
        try:
            url= self.images.url
        except:
            url=''
        return url
    
class Panier(models.Model):
    pass