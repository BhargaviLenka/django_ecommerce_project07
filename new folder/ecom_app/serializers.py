from wsgiref import validate
from rest_framework import serializers
from ecom_app.models import Products_Details, Product_Type, cart_details, Order_list
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        



class CustomerSerializerlogin(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']





# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = "__all__"
#         # extra_kwargs = {
#         #     'password': {'Write-only': True}
#         # }
#     def create(self, validated_data):
#         # password = validated_data.pop('password', None)
#         # instance = self.Meta.model(**validated_data)
#         # if password is not None:
#         #     instance.set_password(password)
#         # instance.save()
#         # return instance
#         return Customer.objects.create(**validated_data)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Type
        fields = "__all__"


# class Myserializer1(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model =employee
#         fields = '__all__'



class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products_Details
        fields = "__all__"



# customer's cart
class CustomerCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart_details
        fields = "__all__"





class CustomerProductCartSer(serializers.ModelSerializer):
    class Meta:
        model = Products_Details
        fields = "__all__"




class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order_list
        fields = "__all__"



# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Order_list
#         fields = "__all__"



