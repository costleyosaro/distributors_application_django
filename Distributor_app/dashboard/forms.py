from django import forms
from Distributor_app.users.models import CustomUser

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']  # Only the profile_picture field will be used



