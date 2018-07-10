# -*- coding: UTF-8 -*-
# 最小二乘法
from math import e  # 引入自然数e
import numpy as np  # 科学计算库
import matplotlib.pyplot as plt  # 绘图库
from scipy.optimize import leastsq  # 引入最小二乘法算法

# 样本数据(Xi,Yi)，需要转换成数组(列表)形式
ti = np.array([  -0.02,0.0,0.02,0.04,0.06,0.08,0.1,0.12,0.14,
               0.16,0.18,0.2,0.22,0.24])
yi = np.array([ 96442484,
               86296681,66141086,56648251, 47694234,41644286,36552084,34877608,32913082,31329971,
               29264199,27870417,26759962,25494653])

# 需要拟合的函数func :指定函数的形状，即n(t)的计算公式
def func(params, t):
   m, p, q = params
   fz = (p * (p + q) ** 2) * e ** (-(p + q) * t)  # 分子的计算
   fm = (p + q * e ** (-(p + q) * t)) ** 2  # 分母的计算
   nt = m * fz / fm  # nt值
   return nt

# 误差函数函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
# 一般第一个参数是需要求的参数组，另外两个是x,y
def error(params, t, y):
   return func(params, t) - y

# k,b的初始值，可以任意设定, 一般需要根据具体场景确定一个初始值
p0 = [0, 5, 9]

# 把error函数中除了p0以外的参数打包到args中(使用要求)
params = leastsq(error, p0, args=(ti, yi))
params = params[0]

# 读取结果
m, p, q = params
print('m=', m)
print('p=', p)
print('q=', q)

# 有了参数后，就是计算不同t情况下的拟合值
y_hat = []
for t in ti:
   y = func(params, t)
   y_hat.append(y)

# 接下来我们绘制实际曲线和拟合曲线
# 由于模拟数据实在太好，两条曲线几乎重合了
fig = plt.figure()
plt.scatter(ti, yi, color='r', label='true')
plt.plot(ti, y_hat, color='b', label='predict')
plt.title('the model(Data from 20180705 09:00am-10:00am)')
plt.xlabel('prefix_threshold')
plt.ylabel('prefetch_flow')
plt.legend()
plt.show()
