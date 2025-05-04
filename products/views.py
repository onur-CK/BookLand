from .models import Book, Category
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import reverse, redirect, get_object_or_404, render
from django.db.models.functions import Lower
from profiles.models import WishlistItem
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.core.paginator import Paginator

def all_products(request):
    """A view to show all products"""
    
    products = Book.objects.filter(available=True)
    query = None
    categories = None
    sort = None
    direction = None
    current_sorting = None
    active_category = None

    if request.GET:
        # Handle categories filter
        if 'category' in request.GET:
            category_name = request.GET['category']
            products = products.filter(category__name=category_name)
            # Get the first matching category instead of requiring uniqueness
            active_category = Category.objects.filter(name=category_name).first()

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

    paginator = Paginator(products, 10)  # Show 10 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
        'search_term': query,
        'active_category': active_category,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    product = get_object_or_404(Book, pk=product_id)
    
    # Check if product is in user's wishlist
    in_wishlist = False
    if request.user.is_authenticated:
        # Check if this product is in the user's wishlist
        in_wishlist = WishlistItem.objects.filter(
            user=request.user, 
            book=product
        ).exists()

    # Get related books (same category)
    related_books = []
    if product.category:
        related_books = Book.objects.filter(
            category=product.category
        ).exclude(id=product.id)[:4]  # Limit to 4 related books

    context = {
        'product': product,
        'related_books': related_books,
        'in_wishlist': in_wishlist,
    }

    return render(request, 'products/product_detail.html', context)


def optimize_image(image):
    """Optimize image size for web display"""
    if not image:
        return None
    
    # Open the image
    img = Image.open(image)
    
    # Calculate new size while maintaining aspect ratio
    max_size = (600, 900)  # Define maximum dimensions for book covers
    img.thumbnail(max_size, Image.LANCZOS)
    
    # Convert to RGB if image has transparency
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    # Save image to buffer
    output = BytesIO()
    img.save(output, format='JPEG', quality=85, optimize=True)
    output.seek(0)
    
    # Return the optimized image
    return InMemoryUploadedFile(
        output, 'ImageField',
        f"{image.name.split('.')[0]}.jpg",
        'image/jpeg',
        sys.getsizeof(output),
        None
    )