"""FHYBLJKM"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import customer_list, Customer1, Product_list_View, Productype, UserLogin, logout_user, CookieUserdetails
from .views import upload_pro_image,AdminProductEdit,DeleteProductAdmin, Customer_Personal_det
from .views import AdminLogin, Place_Order, Buyer_List, Cust_CartDetails,Search
from .views import DeleteUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register('viewset', Customer1, basename='Cust_name')

urlpatterns = [
    path("home/<int:pk>/", customer_list, name="customer_list"),
    path("home/", customer_list, name="customer_list"),
    path('modelview/', include(router.urls)),
    # path('modelview1/', include(router1.urls)),
    path('products/', Product_list_View.as_view(), name="products_list"),
    path('products/<int:product_type_id>', Product_list_View.as_view(), name="products_list"),
    path('product_type/', Productype.as_view(), name="products_list"),
    path('users_login/', UserLogin.as_view(), name="user_login"),
    path('admin_login/', AdminLogin.as_view(), name="user_login"),
    path('post_order/<int:user_id>/', Place_Order.as_view(), name="Orders_list"),
    path('post_order/', Place_Order.as_view(), name="Orders_list"),
    path('buyers/', Buyer_List.as_view(), name="user_list"),
    path('customers/', Buyer_List.as_view(), name="user_list"),
    path('del_cart_details/<int:product_id>/<int:user_id>/<int:delete_id>/',
         Cust_CartDetails.as_view(), name="cart_details"),
    path('cart_details/<int:user_id>/', Cust_CartDetails.as_view(), name="cart_details"),
    path('cart_details/', Cust_CartDetails.as_view(), name="cart_details"),
    path('cart_details/<int:product_id>/<int:user_id>/<int:pro_price>/',
         Cust_CartDetails.as_view(), name="cart_details"),
    path('cart_details/<int:product_id>/<int:user_id>/',
         Cust_CartDetails.as_view(), name="cart_details"),
    path('order_list/<int:user_id>/', Place_Order.as_view()),
    path('auth/', include('rest_framework.urls', namespace='session_auth')),
    path('api-auth/', include('rest_framework.urls')),
    path('search/', Search.as_view(), name='search'),
    path('admin_deleteuser', DeleteUser.as_view(), name='deleteuser'),
    path('changeproimage/', upload_pro_image.as_view(), name="image_upload"),
    path('updproducts/', AdminProductEdit.as_view()),
    path('deleteproductadmin/', DeleteProductAdmin),
    path('order/cancelorder', Place_Order.as_view()),
    path('getproducttype', Productype.as_view()),
    path('getuserperdetails', Customer_Personal_det.as_view()),
    path('order/cancel_order_item', Cust_CartDetails.as_view(), name="cancel_order-item_cart"),


    path('login_cookie/', CookieUserdetails.as_view(), name="user_login"),
    path('logout_cookie/', logout_user.as_view(), name="user_logout"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
