#!/usr/bin/python3
#encoding: utf-8

import requests
import re
from bs4 import BeautifulSoup
import json


#登录获取cookie
login_url = "http://210.30.1.140/index.php/Public/checkLogin"
#登录信息
logindata={
        "txtName":"2015083216",
        "txtPass":"2015083216",
        "txtCheck":"no",
}

#获取cookie
logind = requests.post(login_url,data=logindata)
cookie = logind.cookies


#提交题目
d = {
"submit_language":"1",
"submit_code":"#include <iostream> \n using namespace std;\n int main()\n{int a,b;cin>>a>>b; cout<<a+b<<endl; return 0;}",
"problem_id":"303",
"test_id":"",
"__hash__":"a8edbf0347b55fdb7b7567c1505c15b1_d0ad44986cc057b42f6762993b550404"
}
url = "http://210.30.1.140/index.php/Problems/saveCode"




for i in range(1,3):  #循环填写请求的次数
    r = requests.post(url, data=d,cookies=cookie)


print(r.text)  #返回请求后的内容


'''
requests post请求参考资料：http://blog.csdn.net/junli_chen/article/details/53670887
form形式
json形式
multipat形式
'''
