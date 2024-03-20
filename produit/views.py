from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .form import AuthUser
from .models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def register(request):

    if request.method == "POST":
        form = AuthUser(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.email= form.cleaned_data['email']
            user= form.save()
            print(f"Utilisateur créé : nom: {user.username} password :{user.password} email: {user.email}")
            return redirect("login")
    else:
        form=AuthUser()
    return render(request,"inscription.html",context={"form":form})
    

def loging(request):
    if request.method=="POST":
        usename=request.POST["username"]
        password=request.POST["password"]
        print(password)
        user= authenticate(request, username=usename, password=password)
        context={"username":usename, "password":password}
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "nom ou mot de pass incorect")
    return render(request,"connextion.html")
def home(request):
     return render(request,"base.html")
def base(request):
     return render(request,"home.html")
def logouts(request):
    logout(request)
    return redirect("login")
