# coding:utf-8
import numpy as np

data = np.random.randn(2, 3)
data
# [[ 1.33187815 -0.017561   -0.4074341 ]
#  [-0.09668598  0.21938788 -0.80780985]]
data.shape # 形状（2，3）内嵌两个数组，每个数组三个元素
data.dtype # dtype('float64')

###############################
#       声明数组               #
###############################
#创建一维数组
data_1 = [6, 2, 4, 4]
arr_1 = np.array(data_1)
arr_1   # 一维数组
arr_1.dtype #int64 会自动判断int还是float型(自适应)

data_2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr_2 = np.array(data_2)
arr_2   # 创建二维数组
arr_2.ndim   #  2 ，数组第一维度的大小
arr_2.shape   # (2, 4)

np.zeros(5)  #声明数组，类似C中的声明全0的数组 [ 0.,  0.,  0.,  0.,  0. ] float64
np.zeros((2, 3), dtype=np.int64)
# [[0 0 0]
#  [0 0 0]]
np.arange(15)  #声明数组 ，类似range（15）[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14] int64

#声明数组时，强制声明类型，很实用，类似C中的 int float，哇熟悉的感觉，没有double  int 和 float
arr_1 = np.array([1, 2, 3], dtype=np.float64) # [1. 2. 3.]
arr_1 = np.array([1, 2, 3], dtype=np.int64)  # [1 2 3]
arr_1.astype(np.float64) #强制类型转换

###############################
#       数组计算               #
###############################
#点对点计算，向量化！！！不用写for循环
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr ** 0.5
# array([[ 1.        ,  1.41421356,  1.73205081],
#        [ 2.        ,  2.23606798,  2.44948974]])


###############################
#       基本的索引和切片        #
###############################
#跟C、python的一些用法类似。总结特殊用法
arr = np.arange(10,dtype=np.int64)
arr[5:8] = 12 #[5,8)赋值为12，总结 list切片产生了新的list 而np则不是也就是说改变切片的值，原先的np数组也会被改变，返回的是数组的view
arr[:] = 0 #赋值所有元素为0
#访问2维数组 arr[1][2] 或者 arr[1, 2]我们也可以根据这个进行切片

# bool索引  快捷的处理数据

# 花式索引
#索引跟切片类似，但是索引是得到全新的array
arr = np.array([1, 2, 3, 5, 8], dtype=np.int64)
arr[[0,2]] #[1 3]
#索引和切片不同的是 索引使用 [[  ]]  切片 [:]



###############################
#           通用函数           #
###############################
arr = np.arange(10, dtype=np.int64)
np.sqrt(arr)  #求根
x = np.random.randn(5)
y = np.random.randn(5)
np.maximum(x, y) # 点对点比较x，y的最大值得到新的值






