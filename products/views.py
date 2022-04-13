from django.db.models.query import QuerySet
import products
from django.shortcuts import render
from django.http import HttpResponse
from products.models import Collection, Product, Collection


def index(request):
    queryset = Product.objects.all()
    queryset1 = Collection.objects.all()
    return render(request, 'index.html', {'products': list(queryset), 'collections': list(queryset1)})

def collection(request, title):
    title = Collection.objects.get(id=title)
    queryset = Product.objects.filter(collection = title)
    return render(request, 'collection.html', {'products': list(queryset)})