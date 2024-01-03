from django.shortcuts import render
from products.models import Product, Manifacturer
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.http import JsonResponse

# Create your views here.
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'

# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())} # .values("pk", "name")
    response = JsonResponse(data)
    return response

def manifacturer_list(request):
    manifacturers = Manifacturer.objects.all()
    data = {"manifacturers": list(manifacturers.values())}
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manifacturer": product.manifacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity,
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({"error": {
                "code": 404,
                "message": "Product not found"
                }
            }, status=404)
    return response

def manifacturer_detail(request, pk):
    try:
        manifacturer = Manifacturer.objects.get(pk=pk)
        products = Product.objects.filter(manifacturer=manifacturer).values()
        data = {"manifacturer": {
            "name": manifacturer.name,
            "location": manifacturer.location,
            "active": manifacturer.active,
            "products": list(products)
        }}
        response = JsonResponse(data)
    except Manifacturer.DoesNotExist:
        response = JsonResponse({"error": {
                "code": 404,
                "message": "Manifacturer not found"
                }
            }, status=404)
    return response