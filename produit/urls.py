from django.urls import path,include
from .views import register,loging,logouts,home,base
urlpatterns = [
    path('register/', register,name='register'),
    path('login/',loging, name="login"),
    path('logouts',logouts, name="logouts"),
    path("home", home, name="home"),
    path('base/',base,name="base")
]
