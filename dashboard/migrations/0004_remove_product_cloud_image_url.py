# Generated by Django 5.1.4 on 2025-07-09 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_product_cloud_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cloud_image_url',
        ),
    ]
