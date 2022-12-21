from django.contrib import admin
from django import forms
from .models import Product, Order, Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'description', 'address']
    readonly_fields = ['slug']
    search_fields = ("name__startswith", )
admin.site.register(Company, CompanyAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'description', 'price','created', 'last_updated',]
    readonly_fields = ['slug', 'created', 'last_updated',]
    search_fields = ("name__startswith", )
admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','count','cost','order_by', 'name','address', 'delivered', 'delivered_on', 'created', 'last_updated',]
    readonly_fields = ['slug','order_by', 'created', 'last_updated',]
    search_fields = ("name__startswith", )
admin.site.register(Order, OrderAdmin)


