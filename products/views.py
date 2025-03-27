from django.shortcuts import render

def all_products(request):
    """A view to show all products"""
    return render(request, 'products/products.html')

def product_detail(request):
    """A veiw to show individual product deatails"""
    return render(request, 'products/product_details.html')