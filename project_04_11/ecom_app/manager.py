import json

import jwt
import requests
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password



from rest_framework_simplejwt.tokens import AccessToken


def user_login(request):
    username = request.data['username']
    password = request.data['password']
    print(password, username, password)
    # password = make_password(password)
    print(password)
    # user = authenticate(username=username, password=password)
    user = User.objects.get(username=username)
    # password = make_password(password)
    # user = User.objects.get(username=username)
    print(user.password, make_password(password))


    print(user.password)
    if user:
        is_admin = user.is_superuser
        print(is_admin)
        token_values = requests.post("http://127.0.0.1:8000/api/token/",
                                             {'username': username, 'password': password})
        print(token_values.text)
        data = json.loads(token_values.text)
        print(type(data), data, data)
        cookie_data = Response()
        cookie_data.set_cookie(key="access", value=data['access'], httponly=True, samesite='None', secure=True)
        cookie_data.set_cookie(key="refresh", value=data['refresh'], httponly=True, samesite='None', secure=True)
        cookie_data.set_cookie(key="username", value=username,  samesite='None', secure=True)
        cookie_data.set_cookie(key="is_admin", value=is_admin, samesite='None', secure=True)
        cookie_data.data = {
            'token': token_values,
            "msg": "success"
        }
        print("fjhjolj hiii")
        return cookie_data
    else:
        return Response(json.dumps({"msg": "failedrhbk"}))


def user_details(request):
    # print(request.COOKIES.getAll())
    token = request.COOKIES.get('access')
    # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4MDgwNTcyLCJpYXQiOjE2NjgwODA1MTIsImp0aSI6IjE4MGZkYzc4OGE5OTQ1MjJiZGMzZThlNjljMTNlOWE2IiwidXNlcl9pZCI6OX0.lFincIIV92L6VEEOjW0ZmKB3UWrCY3tozorpCMDh1eU"
    print('payload ' + str(settings.SECRET_KEY))
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        password=make_password(password)
        print(" trying to decode token... \n\n\n")
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY ,algorithms=['HS256'])
        print('payload 1 ' + str(payload))
        user = User.objects.get(id=payload['user_id'])
        # access_token = AccessToken(token)
        password = make_password(password)
        print(password)
        # user = User.objects.get(username=username)
        print(user)
        data = {'user_id': user.id}
        print(type(data))
        print(request.user, "this is user details")
        return data
    except Exception as e:
        return str(e)
    except jwt.ExpiredSignatureError as e:
        return {'error': 'Activations link expired'}
    except jwt.exceptions.DecodeError as e:
        return {'error': 'Invalid Token'}


class UserLoginCookie(APIView):
    pass
