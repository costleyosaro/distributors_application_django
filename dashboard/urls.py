from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import dashboard,flutterwave_webhook, fund_wallet, fund_wallet_callback, upload_profile_picture, mark_single_notification_read, user_performance_data, mark_notifications_read, manage_account, notifications_page, logout_user, Beverage_list, checkout, Care_list, Food_list,Beauty_list, generate_invoice,payment_page, add_to_cart, remove_from_cart,get_csrf_token, cart_data, transaction_history, payment_status  

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_user, name='logout_user'),
    path('Beverage_list/', Beverage_list, name='Beverage_list'),
    path('Food_list/', Food_list, name='Food_list'),
    path('Care_list/', Care_list, name='Care_list'),
    path('generate_invoice/', generate_invoice, name='generate_invoice'),
    path('Beauty_list/', Beauty_list, name='Beauty_list'),
    path('Payment_page/', payment_page, name='payment_page'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('cart-data/', cart_data, name='cart_data'),
    path("transaction-history/", transaction_history, name="transaction_history"),
    path("checkout/", checkout, name="checkout"),
    # path('paystack_webhook/', paystack_webhook, name='paystack_webhook'),
    path('payment_status_<str:invoice_id>/', payment_status, name='payment_status'),
    path('manage-account/', manage_account, name='manage_account'),
    path("user-performance/", user_performance_data, name="user-performance-data"),
    path("notifications/", notifications_page, name="notifications"),
    path("notifications/mark-as-read/", mark_notifications_read, name="mark_notifications_read"),
    path("single-mark-as-read/", mark_single_notification_read, name="mark_single_notification_read"),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('fund_wallet/', fund_wallet, name='fund_wallet'),
    path('fund_wallet_callback/', fund_wallet_callback, name='fund_wallet_callback'),
    path('webhooks_flutterwave/', flutterwave_webhook, name='flutterwave_webhook'),

]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




