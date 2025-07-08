import os
from django.core.management.base import BaseCommand
from django.conf import settings
from dashboard.models import Product  # Adjust if your Product model is in another app
import cloudinary.uploader

class Command(BaseCommand):
    help = 'Migrate product images from local to Cloudinary and store the URLs'

    def handle(self, *args, **options):
        products = Product.objects.filter(cloud_image_url__isnull=True).exclude(image='')

        if not products.exists():
            self.stdout.write(self.style.WARNING("No products found that need migration."))
            return

        for product in products:
            local_path = os.path.join(settings.MEDIA_ROOT, str(product.image))

            if not os.path.exists(local_path):
                self.stdout.write(self.style.ERROR(f"File not found: {local_path}"))
                continue

            try:
                result = cloudinary.uploader.upload(local_path)
                product.cloud_image_url = result['secure_url']
                product.save()
                self.stdout.write(self.style.SUCCESS(f"✅ Uploaded {product.name}: {result['secure_url']}"))

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Failed to upload {product.name}: {str(e)}"))
