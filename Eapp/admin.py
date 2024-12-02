from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'product_name',
        'user',
        'phone_number',
        'product_category',
        'formatted_price',
        'location',
        'product_image_url',
        'created_at',
        
       
        
    )

    # Filter options for the sidebar
    list_filter = (
        'product_category',
        'location',
        'is_sold',
        'created_at',
    )

    # Add search functionality
    search_fields = (
        'product_name',
        'user__username',  # Search by username of the related user
        'phone_number',
        'location',
    )

    # Default ordering of records
    ordering = ('-created_at',)

    # Fields to use as links in the list view
    list_display_links = ('product_name',)

    # Fields editable directly in the list view
    list_editable = ('product_image_url', 'created_at',)

    # Add a date hierarchy for easier navigation
    date_hierarchy = 'created_at'

    # Add read-only fields (for non-editable data)
    readonly_fields = ('created_at', 'updated_at')

    # Customize the detail view of the model
    fieldsets = (
        (None, {
            'fields': ('product_name', 'product_category', 'product_price', 'location', 'user', 'phone_number'),
        }),
        ('Media', {
            'fields': ('product_image_url',),
        }),
        ('Status', {
            'fields': ('is_sold',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

# Register the admin configuration
admin.site.register(Product, ProductAdmin)
