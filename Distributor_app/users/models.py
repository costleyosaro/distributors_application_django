from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings 
from django.conf import settings
from django.core.exceptions import ValidationError

def validate_username_blacklist(username):
    if username.lower() in [name.lower() for name in settings.USERNAME_BLACKLIST]:
        raise ValidationError("This username is not allowed. Please choose another.")


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
   
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    username = models.CharField(
        max_length=150,
        null=True,
        validators=[validate_username_blacklist],  # 👈 Add this
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    name = models.CharField(max_length=255, blank=True, null = True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    NIN = models.CharField(max_length=11, null=True, blank=True)
    date_of_incorporation = models.DateField(blank=True, null= True)
    business_name = models.CharField(max_length=100, blank=True,null=True)
    rc_number = models.CharField(max_length=50, blank=True,null= True)
    years_in_business= models.PositiveIntegerField(blank=True, null=True)
    tin = models.CharField(max_length=50, blank=True, null=True)
    business_address = models.CharField(max_length=100, blank= True, null=True)
    city_lga =  models.CharField(max_length=100, blank=True, null= True)
    directors_name = models.CharField(max_length=100, blank=True, null=True)
    state= models.CharField(max_length=100, blank=True, null=True)
    other_companies = models.CharField(max_length=100, blank=True, null= True)
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []  
    objects = CustomUserManager()

  # Ensure you are using Django's User model


        

        


    
    

    

