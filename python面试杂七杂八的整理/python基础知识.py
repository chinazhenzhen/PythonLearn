'''
集合论set的使用
set是可变类型，不可散列
'''
l1 = [1,2,3,4,5]
l2 = [1,2,3,6]
l3 = list(set(l1)-set(l2)) #交集| 并集& 差集-
print(l3)

'''
列表动态生成字典
'''
key_list = ['a','b','c','ddd']
value_list = [11,22,33]
D = dict(zip(key_list, value_list))
print(D)
#{'a': 11, 'c': 33, 'b': 22}

'''
字典合并
'''
D1 = {'a':1,'b':2, 'c':5}
D2 = {'c':2, 'd':9}
D1.update(D2)
print(D1)
#{'a': 1, 'b': 2, 'c': 2, 'd': 9}
'''
检查字典key值，也可以用in方法
'''
D = {'a':11,'b':22, 'c':33}
print(D.get('d',0)) #不存在时返回的默认值

'''
字符串操作
'''
w = "python is a language"
print(w.find("is"))  #返回第一个字符的下标
print(w.replace("python","ruby")) #字符交换

'''
字符按照长度从大到小排序
'''
l = ['c','cccccc','cccc']
print(sorted(l,key=len,reverse=True))
'''
按照单词逆序的排序结果（单词并没有改变）
'''
l = ['bnana','apple','cherry']
print(sorted(l,key=lambda w:w[::-1]))


'''
单词反转
'''
def r(word):
    return word[::-1]
print(r('dlnu'))
'''
python关闭转义机制
'''
s = r'c:\new\test.py'
print(s) 
#输出c:\new\test.py，加r就不会进行转义

'''
计算阶乘
'''
def f(n):
    return 1 if n<2 else n*f(n-1)
print(f(3))

'''
字典循环与字典推导式
'''
dict = {'a':1,'b':2,'c':3}
for k,v in dict.items():
    print(k,v,end=' ')
dict2 = {k:v for k,v in dict.items() if v%2==1}
print(dict2)
结果：a 1 b 2 c 3 {'a': 1, 'c': 3}

'''
装饰器的简单用法
'''
func_name = []
def save(func):
    func_name.append(func)
    return func
@save
def f1():
    return
@save
def f2():
    return

f1()
f2()
print(func_name)
答案：[<function f1 at 0x02D1C6A8>, <function f2 at 0x050B1468>]

'''
迭代器简单用法
'''
l = [1,2,3,4,5,6,7]
for x in l:
    print(x,end='')
print()
it = iter(l) #使用可迭代对象构建迭代器it
while True:
    try:
        print(next(it))
    except:
        print('none')
        break

'''
生成器简单用法
'''
def gen1():
    for i in range(1,100):
        yield i
for c in gen1():
    print(c)

'''
生成器实现fibonaicc
'''
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n + 1

for i in fib(8):
    print(i)
'''
format函数用法
'''
https://blog.csdn.net/sinat_31824577/article/details/55536336


'''
map filter reduce   用法，增加配合lambda表达式
'''


'''
全局变量 global  作用域问题
'''


'''
@staticmethod和@classmethod
'''
