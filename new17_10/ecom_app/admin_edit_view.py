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
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib import messages
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
# from ecom_app.models import Customer
from ecom_app.serializers import CustomerSerializer, CustomerSerializerlogin, ProductListSerializer, ProductSerializer, \
    CustomerCartSerializer, CustomerProductCartSer, OrderSerializers, Order_cart_serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .renders import UserRenderer
from cloudinary.uploader import upload

# @csrf_exempt
# class AdminDeleteUser(APIView):
#     def post(self,request):
#         print(request.data.get('user_id'))
        # query = User.objects.get(id=request.data.get('user_id'))
        # # query = User.objects.get(id=request.data.get('q'))
        # query.delete()
        # return Response("user has been deleted")
