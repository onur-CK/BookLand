from .models import Book, Category
from django.contrib import messages
# Source: https://docs.djangoproject.com/en/5.1/topics/db/queries/
# Using Django's Q objects for complex queries that can be combined with logical operators
from django.db.models import Q
from django.shortcuts import reverse, redirect, get_object_or_404, render
# Source: https://docs.djangoproject.com/en/5.1/ref/models/database-functions/
# Using Lower database function to perform case-insensitive ordering
from django.db.models.functions import Lower
from profiles.models import WishlistItem
from django.core.paginator import Paginator
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile



def all_products(request):
    """A view to show all products"""
    
    # Source: https://docs.djangoproject.com/en/5.1/topics/db/queries/#retrieving-specific-objects-with-filters
    # Filter books that are available for purchase
    products = Book.objects.filter(available=True)
    query = None
    categories = None
    sort = None
    direction = None
    current_sorting = None
    active_category = None

    # Source: https://docs.djangoproject.com/en/5.1/ref/request-response/#django.http.HttpRequest.GET
    # Handling GET parameters for filtering, searching, and sorting
    if request.GET:
        # Handle categories filter
        if 'category' in request.GET:
            category_name = request.GET['category']
            products = products.filter(category__name=category_name)
            # Get the first matching category
            active_category = Category.objects.filter(name=category_name).first()

        # Handle search queries
        # Source: https://docs.djangoproject.com/en/5.1/topics/db/queries/#complex-lookups-with-q-objects
        # Using Q objects to create complex OR queries across multiple fields
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(title__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query)
            products = products.filter(queries)

        # Handle sorting
        # Source: https://docs.djangoproject.com/en/5.1/ref/models/querysets/#order-by
        # Using order_by method with dynamic field names for flexible sorting
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
            
            # Set current_sorting for template context
            if direction:
                current_sorting = f'{sort}_{direction}'
            else:
                # Default to ascending if no direction
                current_sorting = f'{sort}_asc'  

    # Show 10 products per page
    paginator = Paginator(products, 10)  
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
        'search_term': query,
        'active_category': active_category,
        'current_sorting': current_sorting,  
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    # Source: https://docs.djangoproject.com/en/5.1/topics/http/shortcuts/#get-object-or-404
    # Using get_object_or_404 to retrieve a product or return a 404 error if not found
    product = get_object_or_404(Book, pk=product_id)
    
    # Check if product is in user's wishlist
    in_wishlist = False
    if request.user.is_authenticated:
        # Check if this product is in the user's wishlist
        in_wishlist = WishlistItem.objects.filter(
            user=request.user, 
            book=product
        ).exists()

    # Get related books (same cateogory)
    # Source: https://docs.djangoproject.com/en/5.1/ref/models/querysets/#exclude
    # Using exclude to filter out the current product from related books
    related_books = []
    if product.category:
        related_books = Book.objects.filter(
            category=product.category
        # Limit to 4 related books
        ).exclude(id=product.id)[:4]  

    context = {
        'product': product,
        'related_books': related_books,
        'in_wishlist': in_wishlist,
    }

    return render(request, 'products/product_detail.html', context)


def resize_image(image, size=(300, 450)):
    # Open the uploaded image using PIL
    img = Image.open(image)
    # Ensure the image is in RGB format
    img = img.convert('RGB')
    # Resize the image while maintaining aspect ratio to fit within the specified size
    img.thumbnail(size)
    output = BytesIO()
    # Save the image in JPEG format with 80% quality to balance size and quality
    img.save(output, format='JPEG', quality=80)
    output.seek(0)
    # Return an InMemoryUploadedFile instance that can be saved to a Django ImageField
    return InMemoryUploadedFile(output, 'ImageField', 
                               f"{image.name.split('.')[0]}.jpg", 
                               'image/jpeg', 
                               output.getbuffer().nbytes, None)


