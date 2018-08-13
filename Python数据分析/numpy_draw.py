# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use


m, n = (5, 3)
x = np.linspace(0, 1, m) # 创建等差数列数组 [0,1]分成mf=份
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y) # 类似生成坐标矩阵

plt.style.use('ggplot')
plt.plot(X, Y, marker='.', color='blue', linestyle='none')