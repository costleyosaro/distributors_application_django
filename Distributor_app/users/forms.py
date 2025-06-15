from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Required",
        widget=forms.EmailInput(attrs={'class': 'input-field'}),  # Add CSS here
    )
    phone_number = forms.CharField(
        max_length=11,
        required=True,
        help_text="Required",
        widget=forms.TextInput(attrs={'class': 'input-field'}),  # Add CSS here
    )
    phone_number = forms.CharField(
        max_length=11,
        required=True,
        help_text="Required",
        widget=forms.TextInput(attrs={'class': 'input-field'}),
    )    
    business_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'input-field'}),
    )
    rc_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'input-field'}),
    )
    date_of_incorporation = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'input-field', 'type': 'date'}),
    )
    years_in_business = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input-field'}),
    )
    tin = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'input-field'}),
    )
    business_address = forms.CharField(
        max_length=50,
        widget=forms.Textarea(attrs={'class': 'input-field'}),
    )
    city_lga = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'input-field'}),
    )
    directors_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'input-field'}),
    )
    state = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'input-field'}),
    )
    other_companies = forms.CharField(
        max_length=50,
        widget=forms.Textarea(attrs={'class': 'input-field'}),
    )
    date_of_birth = forms.DateField(
    widget=forms.DateInput(attrs={'class': 'input-field', 'type': 'date'}),
)


    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')
    #     if CustomUser.objects.filter(first_name=first_name).exists():
    #         raise forms.ValidationError("A user with this first name already exists.")
    #     return first_name
    
    class Meta:
        model = CustomUser
        fields = [
            'name', 'username', 'email','date_of_birth', 'phone_number', 'NIN', 'date_of_incorporation',
            'business_name', 'rc_number', 'years_in_business', 'tin',
            'business_address', 'city_lga', 'directors_name', 'state', 'other_companies',
            'password1', 'password2'
        ]
    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data['name']
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'autocomplete': 'new-password'})
        self.fields['password2'].widget.attrs.update({'autocomplete': 'new-password'})
