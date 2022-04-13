from django.contrib import admin
from django.db.models.aggregates import Count
from . import models


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_coun']

    @admin.display(ordering='products_coun')
    def products_coun(self, collection):
        return collection.products_coun
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_coun=Count('product')
        )


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','collection']
    list_editable = ['price']
    list_per_page = 10


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','email']
    list_per_page = 10




