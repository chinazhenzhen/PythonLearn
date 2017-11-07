#!/usr/bin/python3
#encoding: utf-8

import requests
import re
from bs4 import BeautifulSoup
import json


#使用requests的post  不断的项服务器发送请求，form表单要填写正确


#form表单内容  字典形式储存
d = {
"submit_language":"1",
"submit_code":"#include <iostream> \n using namespace std;\n int main()\n{int a,b;cin>>a>>b; cout<<a+b<<endl; return 0;}",
"problem_id":"303",
"test_id":"",
"__hash__":"a8edbf0347b55fdb7b7567c1505c15b1_d0ad44986cc057b42f6762993b550404"
}

url = "http://210.30.1.126/index.php/Problems/saveCode"

#cookie 字典形式储存
cookie ={  #F12 cookie
    "PHPSESSID":"825q744h8419cha2dgh5tvo6a2",
    "uid":"0h4Bfln/yy9r1F+sAx+LAg=="
}


r = requests.post(url,data=d,cookies=cookie)  #发送post请求，data是表单内容，cookies填写cookie

for i in range(1,2):  #循环填写请求的次数
    r = requests.post(url, data=d, cookies=cookie)



print(r.text)  #返回请求后的内容


'''
requests post请求参考资料：http://blog.csdn.net/junli_chen/article/details/53670887

form形式
json形式
multipat形式
'''