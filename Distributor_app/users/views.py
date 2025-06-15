from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from django.contrib.auth import get_user_model
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            send_welcome_email(user)  # Send the email with the HTML template
            messages.success(request, "Registration successful! A welcome email has been sent to your inbox. You can now log in!")
            return redirect('login_view')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()  # Show an empty form for GET request
    return render(request, 'users/Ghadco_ph_register.html', {'form': form})

def send_welcome_email(user):
    subject = "Welcome to Chaimo Multitrade Distributors Portal PHC!☺"
    
    # Load the HTML email template and render it with the user data
    html_message = render_to_string('emails/welcome_email.html', {'user': user})
    plain_message = strip_tags(html_message)  # Fallback to plain text if HTML is not supported
    
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    # Use EmailMultiAlternatives to send both HTML and plain text
    email = EmailMultiAlternatives(subject, plain_message, from_email, recipient_list)
    email.attach_alternative(html_message, "text/html")  # Attach the HTML version
    email.send()





# LOGIN FUNCTION
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Received username: {username}, password: {password}")  # Debugging log
        user = authenticate(request, username=username, password=password)
        if user:
            print(f"Authentication successful for user: {username}")
            login(request, user)
            print(f"User {username} logged in Succesfully!")
            print("Redirecting to dashboard...")
            return redirect('dashboard')
        else:
            print("Invalid credentials!")  # Debugging log
            messages.error(request, 'Invalid credentials! Please try again.')
    return render(request, 'users/Ghadco_PH_Login_renamed.html')




from django.http import HttpResponse
def debug_session_view(request):
    print(f"User authenticated: {request.user.is_authenticated}")  # Debugging
    return HttpResponse("Session debug!")




def REQUEST_template(request):
    if request.method == 'POST':
        # Redirect to the next step when the user clicks the link
        return redirect('forgot_password')
    return render(request, 'users/REQUEST_template.html')



# FORGOT PASSWORD LOGIC
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        CustomUser = get_user_model()  # Get the active user model
        try:
            user = CustomUser.objects.get(email=email)  # Check if email exists in CustomUser model

            # Generate a random 4-digit code
            code = random.randint(1000, 9999)

            # Store the code in the session
            request.session['reset_code'] = code
            request.session['email'] = email

            # Send email with the reset code
            reset_link = f"http://127.0.0.1:8000/users/verify_code/"
            send_mail(
                'Password Reset Request',
                '',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                html_message=render_to_string('users/user_code.html', {
                    'user': user,
                    'reset_link': reset_link,
                    'code': code,
                }),
                fail_silently=False,
            )

            return redirect('verify_code')  # Redirect to verification code page
        except CustomUser.DoesNotExist:
            messages.error(request, "Email address is not registered.")
    return render(request, "users/forgot_password.html")



from django.shortcuts import render, redirect
from django.contrib import messages

def verify_code(request):
    if request.method == "POST":
        # Get the 4-digit code from the form
        digit1 = request.POST.get("digit1")
        digit2 = request.POST.get("digit2")
        digit3 = request.POST.get("digit3")
        digit4 = request.POST.get("digit4")

        # Combine the digits into a single code
        entered_code = f"{digit1}{digit2}{digit3}{digit4}"

        # Retrieve the code stored in the session
        session_code = str(request.session.get("reset_code"))

        # Validate the entered code
        if entered_code == session_code:
            # Code matches; redirect to the reset password page
            return redirect("reset_password")
        else:
            # Code doesn't match; show an error message
            messages.error(request, "Invalid verification code. Please try again.")
    
    # Render the verification page (for both GET and invalid POST)
    return render(request, "users/verify_code.html")



from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
User = get_user_model()

def reset_password(request):
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "reset_password.html")

        # Retrieve the user's email from the session
        email = request.session.get("email")
        if not email:
            messages.error(request, "Session expired. Please try the password reset process again.")
            return redirect("forgot_password")

        try:
            # Get the user using the custom user model
            user = User.objects.get(email=email)
            # Update the user's password
            user.password = make_password(new_password)
            user.save()
            messages.success(request, "Password reset successfully! You can now log in.")
            return redirect("login_view")
        except User.DoesNotExist:
            messages.error(request, "An error occurred. Please try again.")

    return render(request, "users/reset_password.html")





     
