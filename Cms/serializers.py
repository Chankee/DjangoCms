# -*- coding: UTF-8 -*-
'''
@Time: 19年6月5日 下午7:16
@Author: ChanKee
@FileName: serializers.py
@Description: PyCharm
'''
from rest_framework import serializers
from Cms.models import Product,Project

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"