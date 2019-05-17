# -*- coding: UTF-8 -*-
'''
@Time: 19年5月11日 上午11:30
@Author: ChanKee
@FileName: randomcode.py
@Description: 随机生成 6位 字母+数字 的组合
'''
import random
def generate_code():
    str_code = ""
    for i in range(6):
        # num = random.randint(0, 9)
        num = chr(random.randint(48, 57))  # ASCII表示数字
        letter = chr(random.randint(97, 122))  # 取小写字母
        Letter = chr(random.randint(65, 90))  # 取大写字母
        one_code = str(random.choice([num, letter, Letter]))
        str_code += one_code
    return str_code

if __name__ == '__main__':
    code = generate_code()
    print (code)