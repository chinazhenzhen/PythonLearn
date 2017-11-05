#!/usr/bin/python3
#encoding: utf-8

import requests
import re
from bs4 import BeautifulSoup


#利用beautifulsoup解析页面，用requests请求下载页面

#mFile.close()

url = "http://210.30.1.128/JudgeOnline/problemset.php?page="
#对oj平台分析之后，题目网页之间存在一定的联系，爬取不同的页面得到相应的结果


def saveFile(data): #文件保存
  savePath = '/home/h101/chinazz/3.out'
  mFile = open(savePath,'w')   #用二进制写入 时会出现错误
  mFile.write(data)
  mFile.close()


num=1
mstr=""
for i in range(1,4):
    nowurl = ""
    nowurl = url + str(i)

    try:
        res = requests.get(nowurl)    #爬取下载页面
        res.encoding = res.apparent_encoding  #对页面格式进行相应的调整，防止中文乱码
        soup = BeautifulSoup(res.text,"html.parser")  #使用html.parser方式对网页进行解析，soup为解析后的页面


        for x in soup.findAll(name = "a",attrs ={"href":re.compile(r'problem.php')}):#利用正则表达式匹配href中的内容，attrs
            num = num + 1
            try:
                print(x.string) #x代表每条匹配过的a标签，x.string代表a标签中的text属性
                mstr = mstr + x.string +'\n' #
            except:
                print("wrong")
    except:
        break;

saveFile(mstr)

print(num)
