from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_category', 'product_price', 'user')

admin.site.register(Product, ProductAdmin)
