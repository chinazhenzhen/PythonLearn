import requests
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
tmp_str = "12345"


while True:
    response = requests.get(url+tmp_str)
    try:
        reg = re.compile('([0-9]+)')  # 正则匹配数字
        tmp_str = re.findall(reg,response.text)[-1]   #找最后一个
        print(tmp_str)
    except:
        if 'Divide' in response.text:  #中间会有判断，所以加上
            tmp_str = str(int(tmp_str)/2)
        else:
            break

#答案peak.html