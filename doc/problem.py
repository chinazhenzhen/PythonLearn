#!/usr/bin/python3
#encoding: utf-8

import requests
import re
from bs4 import BeautifulSoup
from acmsumdb import ACMREdb



class ACMSUM:
    def __init__(self,name):
        self.name = name
        self.mydb = ACMREdb()
        self.id = self.name[0]
        self.dlnuUrl="http://210.30.1.128/JudgeOnline/userinfo.php?user="+self.name[1]
        self.hduUrl ="http://acm.hdu.edu.cn/userstatus.php?user="+self.name[2]
        self.vjudgeUrl="https://vjudge.net/user/"+self.name[3]
        self.codeforceUrl="http://codeforces.com/profile/"+self.name[4]
        self.dlnuSum = 0
        self.hduSum = 0
        self.vjudgeSum = 0
        self.codeforceMark = 0



    def myRe(self,num):#执行爬虫
        if(num == 1):
            res = requests.get(self.dlnuUrl)  # 爬取下载页面
        if(num == 2):
            res = requests.get(self.hduUrl)
        if(num == 3):
            res = requests.get(self.vjudgeUrl)
        if(num == 4):
            res = requests.get(self.codeforceUrl)

        res.encoding = res.apparent_encoding  # 对页面格式进行相应的调整，防止中文乱码
        soup = BeautifulSoup(res.text, "html.parser")  # 使用html.parser方式对网页进行解析，soup为解析后的页面

        if(num == 1):
            self.getDlnuNum(soup)
        if(num == 2):
            self.getHduNum(soup)
        if(num == 3):
            self.getVjudgeNum(soup)
        if(num == 4):
            self.getCodeforceMark(soup)




    def getDlnuNum(self,soup):
        aDict = soup.findAll(name="a", attrs={'href': 'status.php?user_id=' + self.name[1] + '&jresult=4'})
        try:
            self.dlnuSum = int(aDict[0].string)
        except:
            self.dlnuSum = 0
        self.mydb.updatedb('dlnuojsum',self.dlnuSum,self.id)

    def getHduNum(self,soup):
        tdDict = soup.findAll(name = "td",attrs={'align':'center'})
        try:
            self.hduSum = int(tdDict[7].string)
        except:
            self.hduSum = 0
        self.mydb.updatedb('hduojsum', self.hduSum, self.id)

    def getVjudgeNum(self,soup):
        aDict =  soup.findAll(name = "a",attrs={'title':re.compile('Overall solved')})
        try:
            self.vjudgeSum = int(aDict[0].string)
        except:
            self.vjudgeSum = 0
        self.mydb.updatedb('vojsum', self.vjudgeSum, self.id)

    def getCodeforceMark(self,soup):
        spanDict = soup.findAll(name = "span",attrs={'style':'font-weight:bold;'})
        try:
            self.codeforceMark = int(spanDict[0].string)
        except:
            self.codeforceMark = 0
        self.mydb.updatedb('codeforcerank', self.codeforceMark, self.id)

    def Information(self,):
        for x in range(1,5):
            self.myRe(x)


    def debug(self,):
        print(self.dlnuSum)
        print(self.hduSum)
        print(self.vjudgeSum)
        print(self.codeforceMark)





if __name__ == '__main__':

    giveInfor = ACMREdb()
    Infors = giveInfor.querydbAll()



    for row in Infors:
        Infor = []

        for i in range(0,5):
            num = i*2
            Infor.append(row[num])

        user = ACMSUM(Infor)
        user.Information()
        user.debug()

