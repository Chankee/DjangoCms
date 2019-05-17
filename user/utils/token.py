# -*- coding: UTF-8 -*-
'''
@Time: 19年5月11日 上午10:44
@Author: ChanKee
@FileName: token.py
@Description: 生成token
'''

import hashlib
import time

from user.utils.randomcode import generate_code


def generate_token(username):
    """
    采用自定义key加密
    :param username: 用户名
    :return: 加密的token
    """
    timestamp = str(time.time())
    _code = generate_code()
    token_key = timestamp + username + _code
    token = hashlib.md5()
    token.update(bytes(token_key, encoding='utf-8'))

    return token.hexdigest()
if __name__ == '__main__':
    token = generate_token('pakee')
    print (token)