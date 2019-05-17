# -*- coding: UTF-8 -*-
'''
@Time: 19年5月11日 下午2:05
@Author: ChanKee
@FileName: response.py
@Description: 响应返回定义
'''
KEY_ERROR = {
    "code": "0100",
    "status": False,
    "msg": "请求数据缺失"
}

REGISTER_USERNAME_EXIST = {
    "code": "0101",
    "status": False,
    "msg": "用户名已被注册"
}
REGISTER_PASSWORD_FALSE = {
    "code": "0101",
    "status": False,
    "msg": "两次密码不一致，请重新输入"
}

REGISTER_EMAIL_EXIST = {
    "code": "0101",
    "status": False,
    "msg": "邮箱已被注册"
}

REGISTER_EMAIL_FALSE = {
    "code": "0101",
    "status": False,
    "msg": "邮箱格式有误"
}

REGISTER_SUCCESS = {
    "code": "0000",
    "status": True,
    "msg": "注册成功"
}

SYSTEM_ERROR = {
    "code": "9527",
    "status": False,
    "msg": "系统错误"
}

LOGIN_FAILED = {
    "code": "0103",
    "status": False,
    "msg": "用户名或密码错误"
}

USER_NOT_EXISTS = {
    "code": "0104",
    "status": False,
    "msg": "该用户未注册"
}

LOGIN_SUCCESS = {
    "code": "0001",
    "status": True,
    "msg": "登录成功"
}
