# Generated by Django 4.1 on 2022-10-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0009_alter_order_list_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products_details',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
