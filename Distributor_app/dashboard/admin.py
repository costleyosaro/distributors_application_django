from django.contrib import admin
from django.contrib import admin
from dashboard.models import Product, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')  # ✅ Show important fields in the admin list view
    search_fields = ('name',)  # ✅ Allow searching by name

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'added_at')  # ✅ Show user & product in list view
    list_filter = ('user',)  # ✅ Filter by user
    
    
from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("invoice_id", "user", "product_name", "quantity", "total_price", "added_at")  # Use correct date field
    search_fields = ("invoice_number", "user__username", "product_name")
    list_filter = ("added_at",)  # Use correct date field

    

from django.contrib import admin
from .models import Payment, Products, PaymentItem

class PaymentItemInline(admin.TabularInline):  # You can also use StackedInline
    model = PaymentItem
    extra = 1

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'invoice_id', 'added_at', 'total_amount']
    inlines = [PaymentItemInline]
    list_filter = ('user', 'business_name') # Use PaymentItem as the inline

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock']

@admin.register(PaymentItem)
class PaymentItemAdmin(admin.ModelAdmin):
    list_display = ['payment', 'product', 'quantity']


