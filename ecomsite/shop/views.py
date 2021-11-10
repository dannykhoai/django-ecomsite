from django.shortcuts import render
from .models import Products
# Create your views here.

#shop page
def index(request): 
    product_objects = Products.objects.all()

    #search function
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    return render (request, 'shop/index.html',{'product_objects':product_objects})

#product detail page
def detail(request, id):
    product_object = Products.objects.get(id=id)
    return render (request, 'shop/detail.html',{'product_object':product_object})
