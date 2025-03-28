from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name or self.name
    

