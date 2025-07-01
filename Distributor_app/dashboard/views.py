from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import logging
import os
from django.utils.decorators import method_decorator
from django.conf import settings
logger = logging.getLogger(__name__)
from Distributor_app.users.models import CustomUser  # Import your user model
from django.views.decorators.csrf import csrf_exempt
from Distributor_app.dashboard.models import Product, CartItem
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token
import json
from Distributor_app.dashboard.models import Invoice
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Distributor_app.users.models import CustomUser
import json
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Distributor_app.dashboard.models import Payment

from django.db.models import Q
from Distributor_app.dashboard.models import Product
from django.contrib.auth import logout  

from Distributor_app.dashboard.models import Notification  # ✅ Import Notification model
from django.db.models import Max
from Distributor_app.dashboard.models import Notification  # Make sure this import is at the top



@login_required
def dashboard(request):
    user = request.user

    # 🔥 Get last 5 recent payments
    payments = (
        Payment.objects.filter(user=user)
        .order_by("-added_at")[:5]
        .prefetch_related("payment_items__product")
    )

    # ✅ Count only unread notifications
    unread_count = Notification.objects.filter(user=user, is_read=False).count()

    return render(
        request,
        "dashboard/Ghadco_Users_Dashboard.html",
        {
            "user_name": user.username,
            "payments": payments,
            "unread_count": unread_count  # 🔥 Pass unread count to template
        },
    )











def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})



from django.http import JsonResponse
from Distributor_app.dashboard.models import CartItem, Product  # Ensure correct imports
from django.contrib.auth.decorators import login_required
import json



@login_required
def add_to_cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)
        category = data.get("category", "")

        try:
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user, product=product,
                defaults={"quantity": quantity, "price": product.price}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()

            # Fetch updated cart items for the product's category
            cart_items = list(CartItem.objects.filter(user=request.user, product__category=category).values(
                "product_id", "product__name", "price", "quantity", "product__category"
            ))
            for item in cart_items:
                item["category"] = item.pop("product__category", None)
                item["name"] = item.pop("product__name", "Unknown Product")

            return JsonResponse({
                "message": "Added to cart!",
                "cart_count": CartItem.objects.filter(user=request.user).count(),
                "cart_items": cart_items
            })
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)




from django.http import JsonResponse
from Distributor_app.dashboard.models import CartItem

  # ✅ Allow frontend to send POST requests
from django.views.decorators.csrf import csrf_exempt # Ensure CartItem model is imported




@login_required
def remove_from_cart(request):
    if request.method == "DELETE":
        user = request.user
        product_id = request.GET.get("product_id")

        if not product_id:
            return JsonResponse({"error": "Product ID is required"}, status=400)

        try:
            product_id = int(product_id)
            cart_item = CartItem.objects.filter(user=user, product_id=product_id).first()

            if not cart_item:
                return JsonResponse({"error": "Item not found in cart"}, status=404)

            cart_item.delete()
            return JsonResponse({"message": "Product removed from cart"}, status=200)

        except ValueError:
            return JsonResponse({"error": "Invalid product ID"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)







    
    
from django.http import JsonResponse
from Distributor_app.dashboard.models import CartItem

@login_required
def cart_data(request):
    if request.method == "GET":
        user = request.user
        category = request.GET.get("category")
        if not category:
            return JsonResponse({"error": "Category is required"}, status=400)

        # Fetch cart items for the given category
        cart_items = CartItem.objects.filter(user=user, product__category=category).values(
            "product_id", 
            "product__name", 
            "price", 
            "quantity", 
            "product__category"
        )

        # Format the data to have a "name" field and "category"
        formatted_items = [
            {
                "product_id": item["product_id"],
                "name": item["product__name"],
                "price": item["price"],
                "quantity": item["quantity"],
                "category": item["product__category"]
            }
            for item in cart_items
        ]

        return JsonResponse({"cart_items": formatted_items})
    return JsonResponse({"error": "Invalid request"}, status=400)


def Beverage_list(request):
    beverages = Product.objects.filter(category="Beverage")  # Load all beverage products
    return render(request, 'dashboard/Beverage_list.html', {'products': beverages})







def Food_list(request):
    food = Product.objects.filter(category="Food")  # Load all beverage products
    return render(request, 'dashboard/Food_list.html', {'products': food}) # ✅ Pass search_query





def Care_list(request):
    Care = Product.objects.filter(category="Care")  # Load all beverage products
    return render(request, 'dashboard/Care_list.html', {'products': Care})

from django.shortcuts import render
from django.db.models import Q
from .models import Product  # Ensure Product model is correctly imported

def Beauty_list(request):
    beauty_products = Product.objects.filter(category="Beauty")  # Load all beauty products
    return render(request, 'dashboard/Beauty_list.html', {'products': beauty_products})




@csrf_exempt
@login_required
def manage_account(request):
    if request.method == 'GET':
        return render(request, 'dashboard/Manage_Account_page.html')   # ✅ serve the page on GET

    elif request.method == 'POST':
        print("Request method was:", request.method)
        print('request body:', request.body)
        try:
            data = request.POST
            user = request.user
            # update only fields that are present and non-empty
            fields_to_update = [
                "name", "username", "business_name", "directors_name", "rc_number",
                "tin", "date_of_incorporation", "phone_number", "NIN",
                "email", "business_address", "state", "city_lga"
            ]


            # Update only fields that are present and non-empty
            for field in fields_to_update:
                if field in data and data[field].strip():
                    setattr(user, field, data[field])


            
            user.save()
            logout(request)
            return JsonResponse({
                "message": "Account details updated successfully!",
                "redirect_url": "/login_view/"
            })    
        except Exception as e:
            import traceback
            print("! Exception occured:", e)
            print(traceback.format_exc())
            return JsonResponse({'error': str(e)}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)











import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Distributor_app.dashboard.models import CartItem, Transaction, Payment
from django.db.models import Max  # Import the Invoice model

from Distributor_app.dashboard.models import Payment, PaymentItem
from Distributor_app.dashboard.models import Invoice
from Distributor_app.dashboard.models import CartItem
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def generate_invoice(request):
    """Generates an invoice, saves the transaction, and updates the payment section"""

    if not request.user.is_authenticated:
        return redirect("login_view")

    # Get cart items for the logged-in user
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        print("⚠ No items in cart. Invoice not generated.")
        return redirect("cart_data")  # Redirect back to cart if empty

    # Get the last invoice number for the user and increment it
    last_invoice = Invoice.objects.filter(user=request.user).aggregate(Max("invoice_id"))
    last_number = last_invoice["invoice_id__max"]

    if last_number:
        last_number = int(last_number.split("-")[1])  # Extract the last used number
        new_number = last_number + 1
    else:
        new_number = 1  # Start from 001 if no previous invoice exists

    invoice_id = f"{request.user.id}-{new_number:03d}"  # Format: 5-001, 5-002, etc.

    # Create and save invoice record
    invoice = Invoice.objects.create(user=request.user, invoice_id=invoice_id)

    # Initialize grand total
    grand_total = 0  

    # Create a payment entry (will update later with total)
    payment = Payment.objects.create(
        user=request.user,
        business_name=request.user.business_name,  # Ensure user has business_name
        invoice=invoice,
        product_category="Beverage",  # Change based on actual categories
        amount=0.00,  # Will be updated later
        total_amount=0.00,  # Will be updated later
        grand_total=0.00,  # New field for grand total
        status="pending",  # Change based on logic
    )

    # Loop through cart items and create payment items
    for item in cart_items:
        total_price = item.product.price * item.quantity  # Calculate total per item
        grand_total += total_price  # Add to grand total

        # Create PaymentItem
        PaymentItem.objects.create(
            payment=payment,
            product=item.product,
            quantity=item.quantity,
            total=total_price,  # Store total per item
        )
    # views.py

        from decimal import Decimal, ROUND_HALF_UP

    MAINTENANCE_FEE_PERCENTAGE = Decimal('0.015')

    ...

    maintenance_fee = (grand_total * MAINTENANCE_FEE_PERCENTAGE).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    final_total = grand_total + maintenance_fee

    # Update payment object
    payment.total_amount = grand_total  # Goods only
    payment.maintenance_fee = maintenance_fee
    payment.grand_total = final_total
    payment.save(update_fields=["total_amount", "maintenance_fee", "grand_total"])

    
    # ✅ 🎉 BONUS PRODUCT LOGIC — PLACE IT HERE
    food_product_names = [
        "7 to 7 Choco Gold x 24",
        "7 to 7 COCONUT GOLD x 24",
        "7 TO 7 COOKIES GOLD x 24",
        "7 TO 7 MILKY GOLD x 24"
    ]
    threshold_quantity = 25
    bonus_product = "TOO CLEAN DETERGENT 350g"

    bonus_earned = payment.payment_items.filter(
        product__name__in=food_product_names,
        quantity__gte=threshold_quantity
    ).exists()

    if bonus_earned:
        Notification.objects.create(
            user=request.user,
            message=f"🎉 Hurray {request.user.username}! You've been gifted a {bonus_product}! 🎁",
            notification_type="bonus_product"
        )


        print(f"✅ Invoice {invoice_id} generated with Grand Total: ₦{payment.grand_total}")

    # Clear cart after processing payment
    cart_items.delete()

    # Render the invoice page and pass the invoice ID
    # views.py — render invoice with backend totals
    return render(
        request,
        "dashboard/Invoice_page.html",
        {
            "invoice_id": invoice_id,
            "user": request.user,
            "payment": payment,  # ✅ Add payment object to template
        }
    )







def payment_page(request):
    return render(request,  'dashboard/Payment_page.html')



from django.shortcuts import render
from django.db.models import Q
from Distributor_app.dashboard.models import Payment

def transaction_history(request):
    # Get the filters from the URL parameters
    search_query = request.GET.get("invoice_number", "").strip()  # Invoice filter
    category_query = request.GET.get("category", "").strip()  # Category filter
    invoice_query = request.GET.get("invoice", "").strip()  # Invoice ID filter
    
    # Start with all payments for the user
    payments = Payment.objects.prefetch_related("payment_items__product").filter(user=request.user).order_by("-added_at")
    
    # Apply filters
    if search_query:
        payments = payments.filter(invoice__invoice_id__icontains=search_query)

    if category_query:
        payments = payments.filter(payment_items__product__category__iexact=category_query)  # Filter by category

    if invoice_query:
        payments = payments.filter(invoice__invoice_id__iexact=invoice_query)  # Filter by invoice_id if provided

    print(f"DEBUG: Found {payments.count()} payments for {request.user.username} (Search: '{search_query}', Category: '{category_query}', Invoice: '{invoice_query}')")

    return render(
        request, 
        "dashboard/transactions_history.html", 
        {"payments": payments, "search_query": search_query, "category_query": category_query}
    )










from Distributor_app.dashboard.models import Transaction
import uuid  # Import UUID for unique invoice numbers

def save_transaction(user, cart_items, invoice_id):
    """ Transfers cart items into the transaction history with an invoice number """
    
    for item in cart_items:
        Transaction.objects.create(
            user=user,
            invoice_id=invoice_id,  # Use generated invoice number
            product_name=item.product.name,
            price=item.product.price,
            quantity=item.quantity,
            total_price=item.quantity * item.product.price,
            added_at=item.added_at,
        )


from django.shortcuts import redirect, get_object_or_404
from Distributor_app.dashboard.models import CartItem, Transaction, Invoice  # Import your invoice model
 # Ensure you import Invoice

from django.shortcuts import redirect
from Distributor_app.dashboard.models import CartItem, Transaction, Invoice  

def checkout(request):
    user = request.user
    
    # Ensure there's an existing invoice for this user
    invoice, added = Invoice.objects.get_or_create(user=user)

    cart_items = CartItem.objects.filter(user=user)
    
    for item in cart_items:
        Transaction.objects.create(
            user=user,
            invoice=invoice,  # ✅ This ensures a valid invoice is linked
            product_name=item.product.name,
            product_image=item.product.image,
            price=item.product.price,
            quantity=item.quantity,
            total_price=item.quantity * item.product.price,
        )

    return redirect("generate_invoice")  # Redirect to invoice page after checkout



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from Distributor_app.dashboard.models import Transaction

# PAYSTACK_SECRET_KEY = "sk_test_c6842ff37140097c3c7a8f195ca70c96b233e22a"




# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse, HttpResponseRedirect
# import json
# from .models import Payment, Products, PaymentItem, Transaction
# from django.contrib.auth import get_user_model
# User = get_user_model()  # Correctly reference the swapped user model



# from django.http import JsonResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
# import json
# import re
# from django.http import JsonResponse
# from dashboard.models import Payment, Products, Transaction
# from django.contrib.auth import get_user_model


# @csrf_exempt
# def paystack_webhook(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "Invalid request method"}, status=400)

#     try:
#         data = json.loads(request.body)
#         print("Webhook received!", data)  # Debugging

#         if data.get("event") == "charge.success":
#             payment_data = data.get("data", {})
#             invoice_id = payment_data.get("metadata", {}).get("invoice_id")
#             status = payment_data.get("status")

#             print(f"Received invoice_id: {invoice_id}")  # Debugging
#             if not invoice_id or not isinstance(invoice_id, str):
#                 return JsonResponse({"error": "Invalid or missing invoice_id"}, status=400)

#             if not re.match(r"^\d+-\d+$", invoice_id):
#                 return JsonResponse({"error": "Invalid invoice ID format"}, status=400)

#             amount = payment_data.get("amount", 0)
#             if amount:
#                 amount = int(amount) / 100  # Convert kobo to Naira safely

#             user_id = payment_data.get("metadata", {}).get("user_id")
#             business_name = payment_data.get("metadata", {}).get("business_name")
#             product_category = payment_data.get("metadata", {}).get("product_category")
#             product_details = payment_data.get("metadata", {}).get("products", [])

#             User = get_user_model()
#             try:
#                 user = User.objects.get(id=user_id)
#             except User.DoesNotExist:
#                 return JsonResponse({"error": "User not found"}, status=404)

#             try:
#                 invoice_obj = Invoice.objects.get(invoice_id=invoice_id)
#             except Invoice.DoesNotExist:
#                 return JsonResponse({"error": f"Invoice '{invoice_id}' not found"}, status=404)

#             new_total = sum(product["price"] * product["quantity"] for product in product_details)

#             payment = Payment.objects.create(
#                 user=user,
#                 business_name=business_name,
#                 invoice=invoice_obj,  # ✅ Keep as string in Payment
#                 amount=amount,
#                 total_amount=new_total,
#                 product_category=product_category,
#             )

#             for product in product_details:
#                 product_obj, _ = Products.objects.get_or_create(
#                     name=product["name"],
#                     defaults={"price": product["price"], "category": product_category}
#                 )

#                 Transaction.objects.create(
#                     user=user,
#                     invoice=invoice_obj,  # ✅ Pass instance, not string
#                     product_name=product_obj.name,
#                     product_image="",  # ⚠️ Handle image upload separately
#                     price=product_obj.price,
#                     quantity=product["quantity"],
#                     total_price=product_obj.price * product["quantity"],
#                     status=status
#                 )

#             return JsonResponse({"message": "Payment recorded successfully"}, status=201)

#         return JsonResponse({"message": "Webhook received"}, status=200)

#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON"}, status=400)
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return JsonResponse({"error": "Internal server error"}, status=500)



from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



def logout_user(request):
    logout(request)  # Logs out the user
    return redirect('home')  # Redirects to the home page


from django.http import JsonResponse
from Distributor_app.dashboard.models import Payment  # Import your Payments model

from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from Distributor_app.dashboard.models import Payment
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth, TruncYear


from django.db.models import Sum
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth, TruncYear
from django.http import JsonResponse
from datetime import datetime
from django.utils.timezone import get_current_timezone

from django.utils.timezone import get_current_timezone
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth, TruncYear
from django.db.models import Sum
from django.http import JsonResponse

def user_performance_data(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=403)

    filter_by = request.GET.get("filter_by", "month")
    month = request.GET.get("month")
    year = request.GET.get("year")

    user_payments = Payment.objects.filter(user=request.user)

    if year:
        user_payments = user_payments.filter(added_at__year=year)

    if month:
        user_payments = user_payments.filter(added_at__month=month)

    labels = []
    data = []

    # 🕓 Use local timezone
    tz = get_current_timezone()

    # 📅 Group by Day
    if filter_by == "day":
        user_payments = user_payments.annotate(day_of_week=TruncDay("added_at", tzinfo=tz)) \
            .values("day_of_week") \
            .annotate(total_amount=Sum("total_amount")) \
            .order_by("day_of_week")

        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        data = [0] * 7  # Initialize with 0s

        for entry in user_payments:
            day_index = entry["day_of_week"].weekday()
            data[day_index] = entry["total_amount"]

        labels = days_of_week

    # 📆 Group by Week
    elif filter_by == "week":
        user_payments = user_payments.annotate(week_of_year=TruncWeek("added_at", tzinfo=tz)) \
            .values("week_of_year") \
            .annotate(total_amount=Sum("total_amount")) \
            .order_by("week_of_year")

        for entry in user_payments:
            week_start = entry["week_of_year"].strftime("Week %W (%b %d)")
            labels.append(week_start)
            data.append(entry["total_amount"])

    # 🗓️ Group by Month
    elif filter_by == "month":
        user_payments = user_payments.annotate(month=TruncMonth("added_at", tzinfo=tz)) \
            .values("month") \
            .annotate(total_amount=Sum("total_amount")) \
            .order_by("month")

        labels = [entry["month"].strftime("%B") for entry in user_payments]
        data = [entry["total_amount"] for entry in user_payments]

    # 📈 Group by Year
    elif filter_by == "year":
        user_payments = user_payments.annotate(year=TruncYear("added_at", tzinfo=tz)) \
            .values("year") \
            .annotate(total_amount=Sum("total_amount")) \
            .order_by("year")

        labels = [str(entry["year"].year) for entry in user_payments]
        data = [entry["total_amount"] for entry in user_payments]

    return JsonResponse({"labels": labels, "data": data})


from django.shortcuts import render

def payment_status(request, invoice_id):
    """Display transaction status on the frontend"""
    transaction = Transaction.objects.filter(invoice__invoice_id=invoice_id).first()
    
    if transaction:
        return render(request, "dashboard/payment_status.html", {"transaction": transaction})
    
    return render(request, "dashboard/payment_status.html", {"error": "Transaction not found"})

from django.shortcuts import render
from Distributor_app.dashboard.models import Notification

from django.contrib.auth.decorators import login_required

@login_required
def notifications_page(request):
    try:
        print("🔍 Logged in user:", request.user)

        # Mark all notifications as read
        Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)

        # After marking, unread count should now be 0
        unread_notifications_count = 0

        # Fetch all notifications
        notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')

        return render(request, 'dashboard/notifications.html', {
            'notifications': notifications,
            'unread_notifications_count': unread_notifications_count
        })
    except Exception as e:
        print("💥 ERROR IN NOTIFICATIONS VIEW:", e)
        raise e




@login_required
def mark_notifications_read(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return redirect("notifications")  # or wherever you want to redirect after

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@login_required
def mark_single_notification_read(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            notif_id = data.get("notification_id")
            notif = Notification.objects.get(id=notif_id, user=request.user)
            notif.read = True
            notif.save()

            # ✅ Send updated unread count to the user's WebSocket group
            unread_count = Notification.objects.filter(user=request.user, is_read=False).count()

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"notifications_{request.user.id}",
                {
                    "type": "send_notification",
                    "message": "Notification marked as read",
                    "unread_count": unread_count,
                }
            )

            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request method"}, status=400)



from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Distributor_app.dashboard.forms import ProfilePictureForm  # You'll need to create this form.

@login_required
def upload_profile_picture(request):
    if request.method == 'POST' and request.FILES.get('profile_picture'):
        user = request.user
        user.profile_picture = request.FILES['profile_picture']  # Cloudinary will handle the upload
        user.save()  # Save the image URL to the database
        return redirect('dashboard')  # Redirect to the dashboard or the page you want after upload

    return HttpResponse("Failed to upload profile picture.", status=400)



import requests
import uuid
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.http import JsonResponse
from Distributor_app.dashboard.models import Wallet
import uuid
from django.conf import settings

def create_wallet_if_needed(user):
    """Create a wallet for the user if one doesn't exist."""
    wallet, _ = Wallet.objects.get_or_create(user=user)
    return wallet

from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Distributor_app.dashboard.models import Wallet
from django.urls import reverse
def fund_wallet(request):
    Wallet.objects.get_or_create(user=request.user)

    return render(request, 'dashboard/fund_wallet.html', {
        'callback_url': request.build_absolute_uri(reverse('fund_wallet_callback')),
        'user_email': request.user.email,
        'user_name': request.user.get_full_name() or request.user.username
    })


import requests
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from Distributor_app.dashboard.models import Wallet


def fund_wallet_callback(request):
    status = request.GET.get('status')
    transaction_id = request.GET.get('transaction_id')

    if status == 'successful' and transaction_id:
        try:
            # Verify the transaction with Flutterwave
            verify_url = f"https://api.flutterwave.com/v3/transactions/{transaction_id}/verify"
            headers = {
                "Authorization": f"Bearer {settings.FLW_SECRET_KEY}",
                "Content-Type": "application/json"
            }

            response = requests.get(verify_url, headers=headers)
            data = response.json()

            if data.get("status") == "success" and data["data"].get("status") == "successful":
                amount = float(data["data"]["amount"])
                customer_email = data["data"]["customer"]["email"]

                # Optional but secure: Match transaction email with current user
                if request.user.email != customer_email:
                    return JsonResponse({'error': 'Email mismatch'}, status=403)

                wallet, _ = Wallet.objects.get_or_create(user=request.user)
                wallet.balance += amount
                wallet.save()

                return JsonResponse({'message': 'Wallet funded successfully.'})

            return JsonResponse({'error': 'Payment verification failed'}, status=400)

        except Exception as e:
            return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid or failed payment.'}, status=400)








