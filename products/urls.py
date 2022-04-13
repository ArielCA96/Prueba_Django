from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('collection/<int:title>', views.collection, name='Collection')
]

