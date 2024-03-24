from django.contrib import admin
from .models import ProduitDeal,Grilles,TopProducts
# Register your models here.
admin.site.register(Grilles)

class AdminProduitDeal(admin.ModelAdmin):
    list_display=('name_produit','description','prix','slug')
    search_fields=('name_produit','description','prix','slug')
    ordering=('name_produit','description','prix','slug')
    filter=('name_produit','description','prix','slug')
    list_filter=('name_produit','description','prix','slug')

admin.site.register(ProduitDeal,AdminProduitDeal)


class AdminTopProducts(admin.ModelAdmin):
    list_display=('name_produit','description','prix','slug')
    search_fields=('name_produit','description','prix','slug')
    ordering=('name_produit','description','prix','slug')
    filter=('name_produit','description','prix','slug')
    list_filter=('name_produit','description','prix','slug')
    
admin.site.register(TopProducts, AdminTopProducts)