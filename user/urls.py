# -*- coding: UTF-8 -*-
'''
@Time: 19年5月16日 上午11:35
@Author: ChanKee
@FileName: urls.py
@Description: user 路由配置
'''



from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.Register.as_view()),
    path('login/', views.Login.as_view())
]
