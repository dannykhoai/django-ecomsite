from django.shortcuts import render
from .models import Products
from .models import Order


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
#checkout page

def checkout(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        postalcode = request.POST.get('postalcode',"")
    
        order = Order(name=name, email=email, address=address, city=city,postalcode=postalcode)
        order.save()

    return render(request, 'shop/checkout.html')
