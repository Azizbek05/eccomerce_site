from django.contrib import admin

# Register your models here.
from .models import Category, T_shirts, Buy, Avertising, Register


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug', 'image']

@admin.register(T_shirts)
class T_shirtsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'type', 'character', 'price_type', 'price']
    
    class Meta:
        model = T_shirts


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'products', 'size']

@admin.register(Avertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']