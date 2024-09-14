# Generated by Django 5.0.6 on 2024-09-10 12:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0003_remove_product_updated_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='custom_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(choices=[('electronics', 'Electronics'), ('home_kitchen', 'Home & Kitchen'), ('health_beauty', 'Health & Beauty'), ('jewelry_accessories', 'Jewelry & Accessories'), ('apparel_fashion', 'Apparel & Fashion'), ('food', 'Food'), ('gadgets_computers', 'Gadgets & Computers')], default='electronics', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='Product Name', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='seller_location',
            field=models.CharField(choices=[('school_hostel', 'School Hostel'), ('gate', 'Gate'), ('agbede', 'Agbede'), ('kofesu', 'Kofesu'), ('harmony', 'Harmony'), ('accord', 'Accord'), ('zoo', 'Zoo'), ('oluwo', 'Oluwo'), ('isolu', 'Isolu'), ('camp', 'Camp'), ('custom', 'Other (Custom Location)')], default='school_hostel', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
