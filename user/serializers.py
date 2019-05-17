# -*- coding: UTF-8 -*-
'''
@Time: 19年5月16日 上午11:43
@Author: ChanKee
@FileName: serializers.py
@Description: 用户信息序列化
'''
from rest_framework import serializers
from user import  models
from user.utils import response
import re

from django.contrib.auth.hashers import make_password, check_password



class UserInfoSerializer(serializers.ModelSerializer):
    pass


class CreateUserSerializer(serializers.ModelSerializer):
    confirm_pwd = serializers.CharField(required=True)


    def validate(self, data):
        password = data.get('password')
        confirm_pwd = data.get('confirm_pwd')
        username = data.get('username')
        email = data.get('email')
        if password != confirm_pwd:
            raise serializers.ValidationError(response.REGISTER_PASSWORD_FALSE)
        if models.UserInfo.objects.filter(username=username).first():
            raise serializers.ValidationError(response.REGISTER_USERNAME_EXIST)
        if models.UserInfo.objects.filter(email=email).first():
            raise serializers.ValidationError(response.REGISTER_EMAIL_EXIST)
        if not re.match('^([A-Za-z0-9_\-\.]*)+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$', email):
            raise serializers.ValidationError(response.REGISTER_EMAIL_FALSE)
        return data

    def create(self, validated_data):
        """
                实现create方法
        :param validated_data:
        :return:
        """
        return models.UserInfo.objects.create(
            username = self.validated_data.get('username'),
            password = make_password(self.validated_data.get('password')),
            email = self.validated_data.get('email')
        )

    class Meta:
        model = models.UserInfo
        fields = "__all__"