'''
闭包 = 函数 + 环境变量
闭包 内部有变量有函数  返回函数
内部变量不受外部变量的影响

闭包的意义：
保证闭包内部函数所取的变量不受到全局的一些变量的影响，保证内部函数的正确性
'''

def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve


f = curve_pre()  #将f复制，这样调用 f  就相当与调用  curve 函数
print(f(2))   #100
