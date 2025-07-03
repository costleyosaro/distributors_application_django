from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.timezone import now

User = get_user_model()
# Ensure AUTH_USER_MODEL is used properly




class Product(models.Model):
    CATEGORY_CHOICES = [
        ('beverage', 'Beverage'),
        ('food', 'Food'),
        ('care', 'Care'),
        ('beauty', 'Beauty'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="image_products/", blank=True, null=True)
    rating = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart_items")
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name} for {self.user.username}"


class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoice_id = models.CharField(max_length=10, unique=True, editable=False)  # ✅ Keep as CharField
    added_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            self.invoice_id = self.generate_invoice_id()
        super().save(*args, **kwargs)

    def generate_invoice_id(self):
        # Get last invoice for this user
        last_invoice = Invoice.objects.filter(user=self.user).order_by('-added_at').first()

        if last_invoice:
            last_number = int(last_invoice.invoice_id.split('-')[-1])  # Extract last 3-digit number
            new_number = last_number + 1
        else:
            new_number = 1  # Start from 001 if no invoices exist

        return f"{self.user.id}-{new_number:03d}"  # Format as "UserID-XXX"

    def __str__(self):
        return f"Invoice {self.invoice_id} for {self.user.username}"
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} x{self.quantity}"
    



from django.contrib.auth import get_user_model
User = get_user_model()






class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoice = models.ForeignKey("Invoice", on_delete=models.CASCADE)  # ✅ Changed to ForeignKey
    product_name = models.CharField(max_length=255)
    product_image = models.ImageField(upload_to="transaction_images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ], default='pending') 
    def __str__(self):
        return f"Invoice {self.invoice.invoice_id} - {self.user.username} - {self.status}"



from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)  # Beverage, Food, Care, Beauty
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Ensure the stock field exists

    def __str__(self):
        return self.name

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255, null=True, blank=True)
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, unique=True)  # Unique invoice
    added_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    product_category = models.CharField(max_length=100, default="General")
    maintenance_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Total of items
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Final invoice total

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def calculate_totals(self):
        """Calculate total amount and grand total."""
        total = sum(item.total for item in self.payment_items.all())  # Sum of all item totals
        return total, total  # Right now, grand_total is the same as total_amount

    def save(self, *args, **kwargs):
        """Override save method to update total and grand total before saving."""
        super().save(*args, **kwargs)  # Save first to get primary key
        self.total_amount, self.grand_total = self.calculate_totals()
        super().save(update_fields=['total_amount', 'grand_total'])

    def __str__(self):
        return f"Payment {self.invoice} - {self.business_name} (₦{self.grand_total})"


class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name="payment_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Store price × quantity

    def save(self, *args, **kwargs):
        """Calculate total (price × quantity) before saving."""
        self.total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} (₦{self.total})"

from django.contrib.auth.models import User
from django.utils.timezone import now


class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=50, choices=[
        ("new_registration", "New Registration"),
        ("birthday", "Birthday"),
        ("invoice_created", "Invoice Created"),
        ("payment_success", "Payment Success"),
        ("bonus_product", "Bonus Product"),
        ("incentive", "Incentive"),
    ], default="General")
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"


from django.db import models
from django.conf import settings

class Wallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Wallet"
