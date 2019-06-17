# -*- coding: UTF-8 -*-
'''
@Time: 19年6月17日 下午4:44
@Author: ChanKee
@FileName: response.py
@Description: 响应提示信息
'''
PRODUCT_ADD_SUCCESS = {
    "code": "0001",
    "status": True,
    "msg": "产品添加成功"
}

PRODUCT_EXISTS = {
    "code": "0101",
    "status": False,
    "msg": "该产品已存在"
}

PRODUCT_NOT_EXISTS = {
    "code": "0102",
    "status": False,
    "msg": "产品不存在"
}
