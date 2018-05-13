'''
枚举是一种单例模式
个人总结： 在web开发中，一些根据键值选择的地方，可以使用枚举这个语法。
'''

from enum import Enum


# Enum   name  =  value
class VIP(Enum):
    YELLOW  = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)    # VIP.YELLOW
print(VIP.YELLOW.name) # YELLOW
print(VIP.YELLOW.value) # 1

for v in VIP:  #遍历枚举
    print(v)

#枚举的巧妙用法
a = 1
print(VIP(a))       #VIP.YELLOW
print(VIP(a).name)    #YELLOW