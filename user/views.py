# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import  APIView
from user.utils import response
from user import models
from user import serializers



class Register(APIView):
    """
    注册
    """

    def post(self,request):
        try:
            username = request.data["username"]
            password = request.data["password"]
            confirm_pwd = request.data["confirm_pwd"]
            email = request.data["email"]
        except KeyError:
            return Response(response.KEY_ERROR)


        serializer = serializers.CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(response.REGISTER_SUCCESS)
        else:
            return Response(serializer.errors)
class Login(APIView):
    pass