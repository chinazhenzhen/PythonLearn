import json


json_str = '{"name":"qiyue","age":18}'
#json中的字符串要用双引号

#反序列化，json -》 python
stu = json.loads(json_str)
print(stu)

#序列化 python -》 json
json_str = json.dumps(stu)
print(json_str)
'''
Json  Json不是js的附属品，json是独立的，json可以实现不同语言之间信息的交流
Json对象
Json字符串

JSON是一种数据格式
json是跨语言的
字符串是json的表现形式
'''

'''
json      python
object      dict
array       list
string      str
number      int
number      float
true        True
false       False
null        None
'''