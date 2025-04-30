from django.shortcuts import render

def handler403(request, exception=None):
    """
    Custom 403 Forbidden error handler.
    Displayed when a user tries to access a resource they don't have permission for.
    """
    return render(request, '403.html', status=403)

def handler404(request, exception=None):
    """
    Custom 404 Page Not Found error handler.
    Displayed when a user tries to access a page that doesn't exist.
    """
    return render(request, '404.html', status=404)

def handler500(request, exception=None):
    """
    Custom 405 Method Not Allowed error handler.
    Displayed when a user tries to access a resource with an unsupported request method.
    """
    return render(request, '500.html', status=500)