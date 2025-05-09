# Import the base class for custom Django management commands
from django.core.management.base import BaseCommand
from products.models import Category


class Command(BaseCommand):
    help = 'Creates default book categories if they do not exist'

    def handle(self, *args, **kwargs):
        # List of default categories to create,
        # each with a name and a friendly name
        categories = [
            {'name': 'philosophy', 'friendly_name': 'Philosophy'},
            {'name': 'psychology', 'friendly_name': 'Psychology'},
            {'name': 'self_development', 'friendly_name': 'Self Development'},
            {'name': 'literature', 'friendly_name': 'Literature'},
            {'name': 'biography', 'friendly_name': 'Biography'},
        ]

        # Iterate over the predefined categories
        for category_data in categories:
            # Use get_or_create to avoid duplicate entries.
            # It will get the category if it exists,
            # or create it with the given defaults if it doesn't.
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'friendly_name': category_data['friendly_name']}
            )

            # Output a success message if a new category was created,
            # otherwise inform that it already exists
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Created category: {category.friendly_name}'
                    )
                )
            else:
                self.stdout.write(
                    f'Category already exists: {category.friendly_name}'
                )
        # Final message once all categories have been processed
        self.stdout.write(self.style.SUCCESS('Categories setup complete!'))
