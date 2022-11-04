"""TGHJNML"""
from rest_framework import serializers, exceptions
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAdminUser
from django.contrib import messages
from ecom_app.serializers import CustomerSerializer, Customerserializerlogin, \
    ProductListSerializer, ProductSerializer, \
    CustomerCartSerializer, CustomerProductCartSer, \
    OrderSerializers, Order_cart_serializer, UserPersonalDetails
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from cloudinary.uploader import upload

def login(request):
    """jkhnjkoj"""
    return render(request, 'login.html')

def index(request):
    """jkhnjkoj"""
    return render(request, 'signup.html')

def login1(request):
    """jkhnjkoj"""
    if request.method == "POST":
        x_name = request.POST['name']
        y_n = request.POST['password']
        if User.objects.filter(f_name=x_name).exists():
            if User.objects.get(f_name=x_name).password == y_n:
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
    """jkhnjkoj"""
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
    """jkhnjkoj"""
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
    """jkhnjkoj"""
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


class Product_list_View(APIView):
    """jkhnjkoj"""
    def get(self, request, product_type_id=None):
        """jkhnjkoj"""
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
    """jkhnjkoj"""
    def get(self):
        """jkhnjkoj"""
        queryset = User.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """jkhnjkoj"""
        if request.data.get('user_id') is None:
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({'msg': "error occured"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = request.data.get('user_id')
            queryset = User.objects.get(id=user_id)
            serializer = CustomerSerializer(queryset)
            return Response(serializer.data)


class Customer_Personal_det(APIView):
    def post(self, request):
        """jkhnjkoj"""
        if request.data['user_id'] is not None:
            user_id = request.data['user_id']
            queryset = customer_details.objects.filter(cust_id=user_id)
            serializer = UserPersonalDetails(queryset, many=True)
            print(serializer.data)
            return Response(serializer.data)


# user login
class UserLogin(APIView):
    # renderer_classes=[UserRenderer]
    """jkhnjkoj"""
    def post(self, request):
        """jkhnjkoj"""
        username = request.data['username']
        # email = request.data['email']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            print(user, user.id)
            user_details = User.objects.get(username=username)

            serializer = Customerserializerlogin(user_details)

            return Response({'user_id': user_details.id}, status=status.HTTP_200_OK)

        return Response({'msg': "error occured"}, status=status.HTTP_400_BAD_REQUEST)


class AdminLogin(APIView):
    """jkhnjkoj"""
    # renderer_classes=[UserRenderer]
    # permission_classes = [IsAdminUser]
    def get(self, request):
        """jkhnjkoj"""
        queryset = User.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        """jkhnjkoj"""
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None and IsAdminUser:
            print(user, user.id)
            user_details = User.objects.get(username=username)
            serializer = Customerserializerlogin(user_details)
            return Response({'admin_id': user_details.id}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': "error occured"}, status=status.HTTP_400_BAD_REQUEST)


class Productype(APIView):
    """hello"""
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        """jkhnjkoj"""
        queryset = Product_Type.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        """jkhnjkoj"""
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)


class Cust_CartDetails(APIView):
    """jkhnjkoj"""
    def get(self, request, user_id=None):
        """jkhnjkoj"""
        print(user_id)
        if user_id is None:
            queryset = cart_details.objects.select_related().all()
            serializer = CustomerCartSerializer(queryset, many=True)
            print(serializer.data)
            return Response(serializer.data)

        else:
            print(user_id)
            queryset = cart_details.objects.select_related().filter(customer_id=user_id, order_id=None)
            if queryset:
                serializer = CustomerCartSerializer(queryset, many=True)
                print(serializer.data)
                return Response(serializer.data)
            else:
                return Response({"value": True})

    def post(self, request, product_id=None, user_id=None, order_id=None, pro_price=None):
        """jkhnjkoj"""
        if product_id:
            product = Products_Details.objects.get(id=product_id)
            item_price = product.price
        if request.data.get('order_id') and request.data.get('product_id') and request.data.get('user_id') :
            order_id = request.data.get('order_id')
            product_id = request.data.get('product_id')
            user_id = request.data.get('user_id')
            print(order_id, product_id)
            queryset = cart_details.objects.get(product_id=product_id, order_id=order_id, user_id=user_id)
            queryset.delete()
            return Response({"msg": "item cancelled"})

        if not cart_details.objects.filter(customer_id=user_id, product_id=product_id).exists():
            if product_id is not None and user_id is not None:
                user = User.objects.get(id= user_id)
                product= Products_Details.objects.get(id= product_id)
                x= cart_details(customer_id=user,product_id= product,price_of_item=item_price)
                x.save()
                serializer = CustomerCartSerializer(
                    # {
                    #     "customer_id": user,
                    #     "product_id": product,
                    #     "price_of_item": item_price,
                    #     # "order_id": order_id
                    # }
                    x

                )
                # serializer.is_valid(raise_exception=True)
                # serializer.save()
                print(serializer.data)
                cart = cart_details.objects.get(customer_id=user_id, product_id=product_id)
                x.amounts = x.quantity * item_price
                x.save()
                updated_serializer = CustomerCartSerializer(x)
                return Response(updated_serializer.data)
                # print(serializer.data)
            else:
                raise exceptions.APIException('Invalid Url')
        else:
            cart = cart_details.objects.select_related('customer_id', 'product_id').filter(customer_id=user_id, product_id=product_id)
            print(cart)
            for cartobj in cart:
                print(cartobj.order_id)
                if cartobj.order_id:
                    pass
                else:
                    cartobj.quantity = cartobj.quantity + 1
                    cartobj.amounts = cartobj.quantity * item_price
                    cartobj.save()
                    updated_serializer = CustomerCartSerializer([cartobj], many=True)
                    print(updated_serializer.data)
                    return Response(updated_serializer.data)
            user = User.objects.get(id=user_id)
            product = Products_Details.objects.get(id=product_id)
            new_object_iforderid = cart_details(customer_id=user, product_id=product, price_of_item=item_price)
            new_object_iforderid.save()
            serializer = CustomerCartSerializer(
                # data={
                #     "customer_id": user_id,
                #     "product_id": product_id,
                #     "price_of_item": item_price,
                # }
                new_object_iforderid

            )
            new_object_iforderid.amounts = new_object_iforderid.quantity * item_price
            new_object_iforderid.save()
            updated_serializer = CustomerCartSerializer([new_object_iforderid])
            return Response(updated_serializer.data)

    def delete(self, request, product_id=None, user_id=None, delete_id=None):
        """jkhnjkoj"""
        del_cart = cart_details.objects.filter(customer_id=user_id, product_id=product_id)
        print(del_cart)
        for delobj in del_cart:
            if delobj.order_id:
                pass
            else:
                if delete_id == 0:
                    if delobj.quantity > 1:
                        delobj.quantity = delobj.quantity - 1
                        delobj.amounts = delobj.quantity * delobj.price_of_item
                        delobj.save()
                        updated_serializer = CustomerCartSerializer([delobj], many=True)
                        return Response(updated_serializer.data)
                    if delobj.quantity == 1:
                        delobj.delete()
                        return Response({"msg": "item is removed"})
                if delete_id == 1:
                    delobj.delete()
                    return Response({"msg": "item is "})


# class Orders_list(APIView):
#     def post(self, request, user_id=None):
#         # print(request.POST.get('user_id'))
#         serializer = OrderSerializer(data={
#          "customer_id": 1
#         })
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def get(self, request):
#         queryset = Order_list.objects.all()
#         serializer = OrderSerializer(queryset, many=True)
#         print(serializer.data)
#         return Response(serializer.data)


class Place_Order(APIView):
    """jkhnjkoj"""
    neworder_id = 0

    def post(self, request, user_id=None):
        """jkhnjkoj"""
        if request.data.get('cartarr') is not None:
            print(user_id)
            user = User.objects.get(id=user_id)
            order_cart = Order_list(customer_id=user)
            order_cart.save()
            serializer = OrderSerializers([order_cart], many=True)
            print(serializer)
            print(serializer.data)
            print(request.data)
            ordercartarray = request.data['cartarr']
            print(ordercartarray)
            querysetcart = []
            for i in ordercartarray:
                print(i)
                cartobj = cart_details.objects.get(id=i)
                print(cartobj)
                cartobj.order_id = order_cart
                cartobj.save()
            print(querysetcart)
            return Response({"msg": "success"}, status=status.HTTP_201_CREATED)
        if request.data.get('order_id') is not None:
            obj_id = request.data.get('order_id')
            orderobj = Order_list.objects.get(id=obj_id)
            orderobj.status = True
            orderobj.save()
            return Response({"msg": "cancelled"})

    def get(self, request, user_id=None):
        """jkhnjkoj"""
        # print(request.data.id)
        print(user_id, "huygbfgj")
        order_details = Order_list.objects.filter(customer_id=user_id)
        cartproser = []
        cart_array = []
        serializer = []
        if order_details:
            # for each_cart_product in order_details:
            #     if each_cart_product.status is False:
            #         ordered_products = cart_details.objects.filter(order_id=each_cart_product.id)
            # ordered_products = cart_details.objects.filter(order_id__customer_id=user_id)
            # print(ordered_products)
            serializer = OrderSerializers(order_details, many=True)
            cart_array.append(serializer.data)
            print(cart_array)
            return Response(cart_array)
        else:
            return Response(False)
        #         for each_cart in ordered_products:
        #             print(each_cart)
        #             products_obj = Products_Details.objects.get(id=each_cart.product_id_id)
        #             print(products_obj)
        #             cart_array.append(products_obj)
        #             print(cart_array)
        #         if ordered_products.count == 0:
        #             return Response({"value": True})
        #     cartproser.append(CustomerProductCartSer(cart_array, many=True))
        #     print(cartproser,"fgfcrfbb")
        #     serializer.append(CustomerCartSerializer(ordered_products, many=True))
        #     print(serializer)
        # return Response({"cart": serializer, "cartproducts": cartproser})
        # else:
        #     pass
    # def get(self, request):

    # def post(self, request):
    #     temp = Order_list()
    #     temp.products = request.POST.get('string')
    #     temp.save()
    #     return Response({'msg': "Order Placed"})
    # def get(self, request):
    #     queryset = Order_list.objects.all()


class Search(APIView):
    """jkhnjkoj"""
    def get(self, request):
        """jkhnjkoj"""
        q = request.GET.get('q')
        query = Products_Details.objects.filter(name__icontains=q)
        serializer = ProductListSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        """jkhnjkoj"""
        q = request.data.get('key')
        query = Products_Details.objects.filter(name__icontains=q)
        serializer = ProductListSerializer(query, many=True)
        return Response(serializer.data)


def upload_image(request):
    """jkhnjkoj"""
    file = request.POST.get('image')
    image_payload = upload(file)
    return JsonResponse({
        'imageUrl': image_payload['secure_url']
    })


class upload_pro_image(APIView):
    """jkhnjkoj"""
    def post(self, request):
        """jkhnjkoj"""
        file = request.data.get('image')
        image_payload = upload(file)
        return Response(
            image_payload['secure_url']
        )


# @csrf_exempt
# class AdminDeleteUser(APIView):
#     def get(self,request):
#         print(request.data.get('user_id'))
#         return Response("hii")
#     def post(self,request):
#         print(request.data.get('user_id'))
#         return Response("hii")

class DeleteUser(APIView):
    """jkhnjkoj"""
    def post(self, request):
        """jkhnjkoj"""
        user = request.data.get('user_id')
        query = User.objects.get(id=user)
        query.delete()
        return Response({"msg": "bf"})


class AdminProductEdit(APIView):
    """jkhnjkoj"""
    def post(self, request):
        """jkhnjkoj"""
        if request.data.get('proid') != 0:
            q = request.data.get('details')
            r = request.data.get('productimg')
            proid = request.data.get('proid')
            query = Products_Details.objects.get(id=proid)
            if r is not None:
                query.image = r
            query.name = q['product_name']
            query.price = q['product_price']
            query.stock = q['product_stock']
            query.description = q['product_desc']
            query.save()
            return Response({'msg': 'success'})
        if request.data.get('proid') == 0:
            q = request.data.get('details')
            r = request.data.get('productimg')
            serializer = ProductListSerializer(data={
                "name": q['product_name'],
                "price": q['product_price'],
                "stock": q['product_stock'],
                "description": q['product_desc'],
                "image": r,
                "product_type": request.data['product_type']
            })
            if serializer.is_valid():
                serializer.save()
            return Response({'msg': 'added'})


@api_view(['GET', 'POST'])
def DeleteProductAdmin(request):
    """jkhnjkoj"""
    if request.method == "POST":
        q = request.data.get('product_id')
        query = Products_Details.objects.get(id=q)
        query.delete()
        return Response({'msg': 'Product is removed successfully'})
