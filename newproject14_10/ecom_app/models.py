from datetime import datetime
from enum import unique

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
# from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser,User
from django.utils import timezone

# class employee(models.Model):
#     emp_name = models.CharField(max_length=20)
#     emp_age = models.IntegerField(default=0)
#     emp_number = models.IntegerField(default=000000)
#     emp_address = models.CharField(max_length=200)
#
#     def __str__(self) -> str:
#         return self.emp_name


# Create your models here.

# class Customer(models.Model):
#     cust_id = models.AutoField(primary_key=True)
#     uname = models.CharField(max_length=20)
#     f_name = models.CharField(max_length=25)
#     l_name = models.CharField(max_length=25)
#     mail = models.CharField(max_length=30)
#     password = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.uname


role_choices = (
    ('customer', 'customer'),
    ('seller', 'seller'),
    ('admin', 'admin'),

)

# class User(AbstractBaseUser):
#
#     # role = models.CharField(max_length=30,choices=role_choices, default='customer')
#     def __str__(self):
#         return self.role

class customer_details(models.Model):
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    pin = models.IntegerField(default=0)

# class Order_list(models.Model):
#     ord1_id = models.AutoField(blank=True, primary_key=True)
#     customer_id = models.ForeignKey(User, on_delete=models.CASCADE)




class Product_Type(models.Model):
    name = models.CharField(max_length=25)
    image=models.ImageField(upload_to='image',default=None)
    def __str__(self):
        return self.name

class Products_Details(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE)
    description = models.TextField(blank=True, max_length=255, null=True)
    image = models.TextField(blank=True, null=True)

    # def __str__(self):
    #     return self.name

class Order_list(models.Model):
    # ord1_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Products_Details)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(default=False)


class cart_details(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products_Details, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_of_item = models.FloatField()
    amounts = models.FloatField(null=True)
    order_id = models.ForeignKey(Order_list, null=True, on_delete=models.CASCADE)




class Product_list(models.Model):
    pro_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_type = models.CharField(max_length=25)
    image = models.ImageField(blank=True, upload_to="image", height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name



# class cust_cart_list(models.Model):
#     order_id = models.ForeignKey(Order_list, on_delete=models.CASCADE)
#     product_id = models.ForeignKey(Products_Details, on_delete=models.CASCADE)




# class return_list(models.Model):
#     order_id = models.ForeignKey(Order_list, on_delete=models.CASCADE)
#     product_id = models.ForeignKey(Products_Details, on_delete=models.CASCADE)
#     cust_id = models.ForeignKey(User, on_delete=models.CASCADE)


# class Employees(models.Model):
#     emp_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=25)
#     contact = models.IntegerField()
#     # head_id = models.ForeignKey(Employees , on_delete=models.CASCADE)
#     dept = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.name

# class Total_delivered_items(models.Model):
#     delivery_id = models.AutoField(primary_key=True)
#     emp_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
#     order_id = models.ForeignKey(Order_list, on_delete=models.CASCADE)


# class pickup(models.Model):
#     id = models.AutoField(primary_key=True)
#     brand_name = models.CharField(max_length=30)
#     address = models.CharField(max_length=100)
#     pincode = models.IntegerField()
#
#     def __str__(self):
#         return self.brand_name

# class delivery_person(models.Model):
#     emp_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
#     order_id = models.ForeignKey(Order_list, on_delete=models.CASCADE)


# class Cust_delivered_items(models.Model):
#     cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     order_id = models.ForeignKey(Order_list, on_delete=models.CASCADE)


# class Emp_salary(models.Model):
#     delivery_id = models.ForeignKey(Total_delivered_items, on_delete=models.CASCADE)


# class Seller(models.Model):
#     uname = models.CharField(max_length=20)
#     mail = models.CharField(max_length=30)
#     password = models.CharField(max_length=10)
#     pickup_id = models.ForeignKey(pickup, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
