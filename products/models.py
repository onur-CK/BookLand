from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name or self.name
    
class Book(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True,
                                 validators=[MinValueValidator(0), MaxValueValidator(5)])
    image = models.ImageField(null=True, blank=True)
    inventory = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.image:
            # Save original image first
            super().save(*args, **kwargs)
            
            # Create optimized versions in multiple sizes
            img = Image.open(self.image.path)
            
            # Define image sizes (thumbnail, small, medium)
            sizes = {
                'thumbnail': (150, 225),  # For cart/small components
                'small': (250, 375),      # For product cards
                'medium': (400, 600)      # For product detail
            }
            
            # Create optimized JPG and WebP versions for each size
            img_name = self.image.name.split('.')[0]
            img_path = self.image.path.split('.')[0]
            
            for size_name, dimensions in sizes.items():
                # Create sized version
                sized_img = img.copy()
                sized_img.thumbnail(dimensions, Image.LANCZOS)
                
                # Save WebP version (better compression)
                webp_path = f"{img_path}_{size_name}.webp"
                sized_img.save(webp_path, 'WEBP', quality=85)
                
                # Save JPG version (fallback)
                jpg_path = f"{img_path}_{size_name}.jpg"
                sized_img = sized_img.convert('RGB')
                sized_img.save(jpg_path, 'JPEG', quality=85, optimize=True)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

