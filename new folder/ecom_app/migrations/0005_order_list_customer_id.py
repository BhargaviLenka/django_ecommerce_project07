# Generated by Django 4.1 on 2022-10-17 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom_app', '0004_alter_cart_details_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_list',
            name='customer_id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
