# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 4:41 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : debugtalk.py
# @Software: PyCharm

import random
import string
from faker import Faker


def get_faker_count(count):
    f = Faker(locale='zh_CN')
    name_listr = []
    for i in range(0, count):
        name_listr.append(f.name())  # 姓名
        name_listr.append(f.province())  # 省份
        name_listr.append(f.company())  # 公司名
        name_listr.append(f.phone_number())  # 手机号码
    return name_listr


def keyword():
    return "新梦想"


def keylist():
    return ['java', 'python', 'jmeter']


def get_phone():
    prelist = ['130', '136', '138', '137', '150', '155', '158', '177', '186', '185']
    phone = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
    return phone


def create_phone():
    prelist = ['130', '136', '138', '137', '150', '155', '158', '177', '186', '185']
    rephone = random.choice(prelist)
    last = "".join(random.sample(string.digits, 8))
    return rephone + last


if __name__ == "__main__":
    print(get_phone())
    print(create_phone())
    print(get_faker_count(3))
