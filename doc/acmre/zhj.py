#!/usr/bin/python3
# encoding: utf-8

import requests
import re
from bs4 import BeautifulSoup


def saveFile(data):  # 文件保存
    savePath = '/home/h101/chinazz/acmre/templates/RE.html'
    mFile = open(savePath, 'w')  # 用二进制写入 时会出现错误
    mFile.write(data)
    mFile.close()


# 使用requests的post  不断的项服务器发送请求，form表单要填写正确


# form表单内容  字典形式储存

def myre(dict):
    logind = {
        "ldap": "auth",
        "zjh": dict["xuehao"],
        "mm": dict["zhjmm"]
    }

    loginoutd = {
        "loginType": "platformLogin"
    }

    url1 = "http://zhjw.dlnu.edu.cn/loginAction.do"
    url2 = "http://zhjw.dlnu.edu.cn/xkAction.do?actionType=17"
    url3 = "http://zhjw.dlnu.edu.cn/logout.do"
    # cookie 字典形式储存
    cookie = {  # F12 cookie
        "JSESSIONID": "abcBidDHzmO-g6G5yRg-v"
    }

    rin = requests.post(url1, data=logind, cookies=cookie)
    r = requests.post(url2, cookies=cookie)  # 发送post请求，data是表单内容，cookies填写cookie
    rout = requests.post(url3, data=loginoutd, cookies=cookie)

    soup = BeautifulSoup(r.text, "html.parser")
    src = soup.findAll(name='td')

    saveFile(r.text)


'''
requests post请求参考资料：http://blog.csdn.net/junli_chen/article/details/53670887

form形式
json形式
multipat形式
'''