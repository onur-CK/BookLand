from django.shortcuts import render

def all_products(request):
    return render(request, 'products/products.html')

def product_detail(request):
    return render(request, 'products/product_details.html')