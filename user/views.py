# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import  APIView
from user.utils import response
from user import models
from user import serializers
from django.contrib.auth.hashers import  check_password
from user.utils.token import generate_token
from django.core.exceptions import ObjectDoesNotExist


class Register(APIView):
    """
    注册
    """

    def post(self,request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            confirm_pwd = request.data.get("confirm_pwd")
            email = request.data.get("email")
        except KeyError:
            return Response(response.KEY_ERROR)


        serializer = serializers.CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response.REGISTER_SUCCESS)
        else:
            return Response(serializer.errors)
class Login(APIView):
    """
    登录
    """
    def post(self,request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
        except KeyError:
            return Response(response.KEY_ERROR)

        user = models.UserInfo.objects.filter(username=username).first()

        if not user:
            return Response(response.USER_NOT_EXISTS)
        if not check_password(password,user.password):
            return Response(response.LOGIN_FAILED)

        token = generate_token(username)

        try:
            models.UserToken.objects.update_or_create(user=user, defaults={"token": token})
        except ObjectDoesNotExist:
            return Response(response.SYSTEM_ERROR)
        else:
            response.LOGIN_SUCCESS["token"] = token
            response.LOGIN_SUCCESS["user"] = username
            return Response(response.LOGIN_SUCCESS)