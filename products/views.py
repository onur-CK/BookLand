from .models import Book, Category
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import reverse, redirect, get_object_or_404, render
from django.db.models.functions import Lower

def all_products(request):
    """A view to show all products"""
    
    products = Book.objects.filter(available=True)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Handle categories filter
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle search queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query)
            products = products.filter(queries)

        # Handle sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """A veiw to show individual product deatails"""
    product = get_object_or_404(Book, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html')
