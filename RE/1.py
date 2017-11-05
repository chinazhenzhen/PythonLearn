#!/usr/bin/python3
#encoding:utf-8
import urllib.request

import urllib.request

# 抓取静态网页    模拟浏览器登录  保存文件
def saveFile(data): #文件保存
  savePath = '/home/h101/chinazz/1.out'
  mFile = open(savePath,'wb')
  mFile.write(data)
  mFile.close()

url = 'http://www.baidu.com/'
req = urllib.request.Request(url, headers={
  'Connection': 'Keep-Alive',
  'Accept': 'text/html, application/xhtml+xml, */*',
  'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}) #模拟浏览器
oper = urllib.request.urlopen(req)
data = oper.read()
saveFile(data)