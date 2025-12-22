from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 2
    template_name = "products/product_list.html"


class ProductDetailView(ListView):
    queryset = Product.objects.select_related("name", "description")
    model = Product
    context_object_name = 'products'
    template_name = "products/product_detail.html"
