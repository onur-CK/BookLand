from django.core.management.base import BaseCommand
from products.models import Category

class Command(BaseCommand):
    help = 'Creates default book categories if they do not exist'

    def handle(self, *args, **kwargs):
        categories = [
            {'name': 'philosophy', 'friendly_name': 'Philosophy'},
            {'name': 'psychology', 'friendly_name': 'Psychology'},
            {'name': 'self_development', 'friendly_name': 'Self Development'},
            {'name': 'literature', 'friendly_name': 'Literature'},
            {'name': 'biography', 'friendly_name': 'Biography'},
        ]

        for category_data in categories:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'friendly_name': category_data['friendly_name']}
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.friendly_name}'))
            else:
                self.stdout.write(f'Category already exists: {category.friendly_name}')
        
        self.stdout.write(self.style.SUCCESS('Categories setup complete!'))