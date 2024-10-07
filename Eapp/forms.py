from django.contrib.auth.models import User
from django import forms
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from .models import Product

class CustomRegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, validators=[EmailValidator()])
    phone = forms.CharField(
        required=True,
        validators=[RegexValidator(regex=r'^\d{10,15}$', message="Phone number must be 10-15 digits.")]
    )
    password = forms.CharField(widget=forms.PasswordInput())
    confirmpassword = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'confirmpassword']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirmpassword")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirmpassword', "Passwords do not match.")
        
        return cleaned_data

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  # Set email as username
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'product_category', 'product_price', 'phone_number', 'location']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'product_image': forms.FileInput(attrs={'class': 'form-control', 'required': 'required'}),
            'product_category': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
            'product_price': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control', 
                'required': 'required', 
                'value': '+234',  # Pre-fill with +234
                'readonly': 'readonly',  # Make +234 uneditable
                'pattern': r'\+234\d{10}',  # Ensure it matches Nigerian phone numbers
                'placeholder': '+234'  # Show +234 in the field as a placeholder
            }),
            'location': forms.Select(attrs={'class': 'form-select', 'required': 'required'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

    # Ensure the entered phone number is exactly 10 digits
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValidationError('Phone number must be 10 digits long.')
    
    # Prepend +234 to the phone number
        return f'+234{phone_number}'