#!/usr/bin/python3
#encoding: utf-8

import requests
import re
from bs4 import BeautifulSoup


#使用cookie登录网站，并且抓取相应的数据

url = "http://210.30.1.126/index.php/Sidebar/showState"
cookie ={  #F12 cookie
    "PHPSESSID":"8p7uskd1ao8mq978609u2jbcq6",
    "uid":"0h4Bfln/yy9r1F+sAx+LAg=="
}

res = requests.get(url,cookies=cookie)    #爬取下载页面,爬取页面是加入cookie
res.encoding = res.apparent_encoding  #对页面格式进行相应的调整，防止中文乱码
soup = BeautifulSoup(res.text,"html.parser")  #使用html.parser方式对网页进行解析（解析的下載的text格式），soup为解析后的页面

for child in soup.findAll(name='a'):
    print(child)

