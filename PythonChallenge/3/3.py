import re
import requests

response = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
data = response.text

reg = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]') #正则表达式

ans = ""
for i in reg.findall(data):
    ans += i

print(ans)
#linkedlist