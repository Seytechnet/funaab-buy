from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('home_kitchen', 'Home & Kitchen'),
        ('health_beauty', 'Health & Beauty'),
        ('jewelry_accessories', 'Jewelry & Accessories'),
        ('apparel_fashion', 'Apparel & Fashion'),
        ('food', 'Food'),
        ('gadgets_computers', 'Gadgets & Computers'),
    ]

    LOCATION_CHOICES = [
        ('school hostel', 'School Hostel'),
        ('gate', 'Gate'),
        ('agbede', 'Agbede'),
        ('kofesu', 'Kofesu'),
        ('harmony', 'Harmony'),
        ('accord', 'Accord'),
        ('zoo', 'Zoo'),
        ('oluwo', 'Oluwo'),
        ('isolu', 'Isolu'),
        ('camp', 'Camp'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, blank=True)  # Add location field
    created_at = models.DateTimeField(auto_now_add=True)  # Only use auto_now_add
    updated_at = models.DateTimeField(auto_now=True)
    is_sold = models.BooleanField(default=False) 
    def __str__(self):
        return self.product_name if self.product_name else 'Unnamed Product'
