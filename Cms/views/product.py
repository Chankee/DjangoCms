from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from Cms.models import Product
from rest_framework.response import Response
from Cms.serializers import ProductSerializer
from Cms.utils.response import *

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #重写create方法
    def create(self, request, *args, **kwargs):
        product_name = request.data['name']

        if self.queryset.filter(name=product_name).first():
            return Response(PRODUCT_EXISTS)
        # 反序列化
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(PRODUCT_ADD_SUCCESS)



