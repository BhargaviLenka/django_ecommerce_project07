# Generated by Django 4.1 on 2022-10-13 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0003_order_list_cart_details_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_details',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_app.order_list'),
        ),
    ]