from django.urls import path,include
from .views import register,loging,logouts,home,base,produit,detail,topdetails
urlpatterns = [
    path('register/', register,name='register'),
    path('login/',loging, name="login"),
    path('logouts/',logouts, name="logouts"),
    path("home/", home, name="home"),
    path('bare/',base,name="base"),
    path('produit/',produit,name="produit"),
    path('detail/<slug>/',detail, name="detail"),
    path('topdetails/<slug>/',topdetails,name="topdetail")
]
