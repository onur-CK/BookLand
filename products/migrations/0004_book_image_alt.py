# Generated by Django 5.1.7 on 2025-05-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image_alt',
            field=models.CharField(blank=True, help_text='Alternative text for image (important for SEO and accessibility)', max_length=255, null=True),
        ),
    ]
