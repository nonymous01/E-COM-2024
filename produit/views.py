from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .form import AuthUser
from .models import User,Grilles,ProduitDeal,TopProducts
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

# def grille(request,*args, **kwargs):
#     grilles= Grilles.objects.all()
#     context={'grilles':grilles}
#     return render(request,"base.html", context)

def produit(request):
    produits= ProduitDeal.objects.all()
    grilles=Grilles.objects.all()
    topproducts= TopProducts.objects.all()
    context={
        "produits":produits,
        "grilles":grilles,
        "topproducts":topproducts
        }
    return render(request,"base.html", context)





# def voirarticle(request):
#     if request.method == "POST":
#         name= request.POST.get("name_produit")
#         print(name)
#         description= request.POST.get("description")
#         print(description)
#         prix= request.POST.get("prix")
#         print(prix)
#         image= request.POST.get("image")
#         context={
#             "name":name,
#             "description":description,
#             "prix":prix,
#             "image":image
#         }
#         return render(request, "voirarticle.html", context)
#     return render(request, "voirarticle.html")
def detail(request,slug:str):
        detail= get_object_or_404(ProduitDeal,slug=slug)
        return render(request, "voirarticle.html",{"detail":detail,})

def topdetails(request, slug:str):
    topdetail= get_object_or_404(TopProducts,slug=slug)
    return render(request, "topdetail.html",{"topdetail":topdetail})

    




#authentifications
def home(request):
     return render(request,"panier.html")
def base(request):
     return render(request,"bare.html")
def logouts(request):
    logout(request)
    return redirect("login")

