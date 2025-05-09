from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Main URL patterns
# Source: https://docs.djangoproject.com/en/5.1/topics/http/urls/
urlpatterns = [
    # Django admin interface - provides management UI for authorized users
    path('admin/', admin.site.urls),

    # Authentication URLs provided by django-allauth
    # (login, signup, password reset, etc.)
    path('accounts/', include('allauth.urls')),

    # Home app - handles landing page and main site information
    path('', include('home.urls')),

    # Products app - book catalog, details, and browsing functionality
    path('products/', include('products.urls')),

    # Profiles app - user account management, order history, and wishlist
    path('profile/', include('profiles.urls')),

    # Shopping cart functionality
    path('cart/', include('cart.urls')),

    # Checkout process and order management
    path('checkout/', include('checkout.urls')),

    # Extra pages like FAQ, contact, policies, etc.
    path('extra_pages/', include('extra_pages.urls')),

    path('newsletter/', include('newsletter.urls')),

# Static/media file serving for development (not for production use)
# Source: https://docs.djangoproject.com/en/5.1/howto/static-files/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

# Register custom error handlers
# Source: https://docs.djangoproject.com/en/5.1/topics/http/views/#customizing-error-views
handler403 = 'bookland.handlers.handler403'
handler404 = 'bookland.handlers.handler404'
handler500 = 'bookland.handlers.handler500'
