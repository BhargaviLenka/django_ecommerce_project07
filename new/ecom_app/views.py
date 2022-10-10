from itertools import count
import json
from queue import Empty
from rest_framework import serializers, exceptions
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from httplib2 import Authentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib import messages
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# from ecom_app.models import Customer
from ecom_app.serializers import CustomerSerializer, CustomerSerializerlogin, OrderSerializer, ProductListSerializer, ProductSerializer, \
    CustomerCartSerializer, CustomerProductCartSer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .renders import UserRenderer
from cloudinary.uploader import upload

# # Create your views here.
# from ..templates import *

def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'signup.html')


def login1(request):
    if request.method == "POST":
        x = request.POST['name']
        y = request.POST['password']
        if User.objects.filter(f_name=x).exists():
            if User.objects.get(f_name=x).password == y:
                return render(request, 'home.html')
            else:
                return HttpResponse("no output")
        else:
            return HttpResponse("Username doesn't match")
    else:
        return render(request, 'login.html')


# def login(request):
#     if request.method=='POST':
#         obj=Customer()
# def xyz(request, exception):
#     return render(request, 'login.html', status=404)


def signup(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        mail = request.POST['email']
        password = request.POST['password']
        conf_pass = request.POST['confirm_password']
        a = request.POST['person']
        # img = request.POST['img']
        if password == conf_pass:
            if a == "buyer":
                if User.objects.filter(uname=uname).exists():
                    if User.objects.filter(mail=mail).exists():
                        messages.info(request, 'username or mail already exists')
                        return redirect('signup')
                else:
                    if User.objects.filter(mail=mail).exists():
                        messages.info(request, 'username or mail already exists')
                        return redirect('signup')
                    else:
                        x = User.objects.create(uname=uname, f_name=f_name, l_name=l_name, mail=mail,
                                                password=password)
                        x.save()
                        return render(request, 'home.html')
            if a == "seller":
                return HttpResponse("Welcome  " + uname)
        else:
            messages.info(request, 'Password doesnot matches')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


@api_view(['GET', 'POST'])
# @csrf_exempt
# @permission_classes((permissions.AllowAny,))
def customer_list(request, pk=None):
    id = pk
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print(pk)
        cust = User.objects.filter(cust_id=2)
        print("customer id is: ", cust)
        serializer = CustomerSerializer(cust, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request)
        # data = JSONParser().parse(request)

        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class Customer1(ModelViewSet):
    x = User.objects.all()
    queryset = x
    serializer_class = CustomerSerializer


# class employeeViewModelset1(ModelViewSet):
#     queryset = employee.objects.all()
#     serializer_class = Myserializer1
# permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# def highlight(self, request, *args, **kwargs):
#     snippet = self.get_object()
#     return Response(snippet.highlighted)
#
# def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)


class Product_list(APIView):
    def get(self, request, product_type_id=None):
        if product_type_id is None:
            queryset = Products_Details.objects.all()
            serializer = ProductListSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Products_Details.objects.filter(product_type=product_type_id)
            serializer = ProductListSerializer(queryset, many=True)
            return Response(serializer.data)


# user signup
class Buyer_List(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'msg': "error occured"}, status=status.HTTP_400_BAD_REQUEST)


# user login
class UserLogin(APIView):
    # renderer_classes=[UserRenderer]
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            print(user, user.id)
            user_details = User.objects.get(username=username)

            serializer = CustomerSerializerlogin(user_details)

            return Response({'user_id': user_details.id}, status=status.HTTP_200_OK)

        return Response({'msg': "error occured"}, status=status.HTTP_400_BAD_REQUEST)


class Productype(APIView):
    def get(self, request):
        queryset = Product_Type.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)


class Cust_CartDetails(APIView):
    def get(self, request, user_id=None ):
        print(user_id)
        queryset = cart_details.objects.filter(customer_id=user_id)
        cart_array = []
        print(queryset)
        for each_cart in queryset:
            # print(each_cart)
            products_obj = Products_Details.objects.get(id=each_cart.product_id_id)
            print(products_obj)
            cart_array.append(products_obj)
            # print(cart_array)
        if queryset is None:
            return Response({"value": True})
        # print(cart_array)
        cartproser = CustomerProductCartSer(cart_array, many=True)
        # print(cartproser.data)
        serializer = CustomerCartSerializer(queryset, many=True)
        # print(serializer.data)
        return Response({"cart":serializer.data, "cartproducts": cartproser.data})

    def post(self, request, product_id=None, user_id=None, pro_price=None):
        product=Products_Details.objects.get(id=product_id)
        item_price = product.price
        if not cart_details.objects.filter(customer_id=user_id, product_id=product_id).exists():
            if product_id is not None and user_id is not None:
                serializer = CustomerCartSerializer(
                    data={
                        "customer_id" : user_id,
                        "product_id" : product_id,
                        "price_of_item" : pro_price
                    }
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()
                cart = cart_details.objects.get(customer_id=user_id, product_id=product_id)
                cart.amounts = cart.quantity * cart.price_of_item
                cart.save()
                updated_serializer = CustomerCartSerializer([cart], many=True)
                return Response(updated_serializer.data)
                # print(serializer.data)
            else:
                raise exceptions.APIException('Invalid Url')
        else:
            cart = cart_details.objects.get(customer_id=user_id, product_id=product_id)
            cart.quantity = cart.quantity + 1
            cart.amounts = cart.quantity * cart.price_of_item
            cart.save()
            updated_serializer = CustomerCartSerializer([cart], many=True)
            return Response(updated_serializer.data)
            # return Response("serializer.data")
    def delete(self, request, product_id=None, user_id=None,delete_id=None):
        del_cart = cart_details.objects.get(customer_id=user_id, product_id=product_id)
        if delete_id == 0:
            if del_cart.quantity > 1:
                del_cart.quantity = del_cart.quantity - 1
                del_cart.amounts = del_cart.quantity * del_cart.price_of_item
                del_cart.save()
                updated_serializer = CustomerCartSerializer([del_cart], many=True)
                return Response(updated_serializer.data)
            if del_cart.quantity == 1:
                del_cart.delete()
                return Response({"msg": "item is removed"})
        if delete_id == 1:
            del_cart.delete()
            return Response({"msg": "item is removed"})

class Orders_list(APIView):
    def post(self, request, user_id=None):
        # print(request.POST.get('user_id'))
        serializer = OrderSerializer(data={
         "customer_id": 1
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        queryset = Order_list.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)



class Place_Order(APIView):
    def post(self, request):
        temp = Order_list()
        temp.products = request.POST.get('string')
        temp.save()
        return Response({'msg': "Order Placed"})
    def get(self, request):
        queryset = Order_list.objects.all()



def upload_image(request):
    file = request.FILES['image']
    image_payload = upload(file)
    return JsonResponse({
        'imageUrl': image_payload['secure_url']
    })