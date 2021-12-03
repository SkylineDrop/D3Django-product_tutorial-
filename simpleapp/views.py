from django.views.generic import ListView, DetailView

from .models import Product

class ProductsList(ListView):
    model = Product
    template_name = 'products.html' 
    context_object_name = 'products'

class ProductDetail(DetailView):
    model = Product
    template_name = 'products.html' 
    context_object_name = 'products'