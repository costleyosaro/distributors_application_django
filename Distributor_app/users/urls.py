from django.urls import path
from Distributor_app.users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('REQUEST_template/', views.REQUEST_template, name='REQUEST_template'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('debug-session/', views.debug_session_view, name='debug_session_view'),
]

    


