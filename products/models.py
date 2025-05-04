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
            # Save original image
            super().save(*args, **kwargs)
            
            # Create WebP version
            img = Image.open(self.image.path)
            webp_path = f"{self.image.path.split('.')[0]}.webp"
            img.save(webp_path, 'WEBP', quality=85)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"
    

