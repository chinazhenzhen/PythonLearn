import pickle
'''
pickle模块使用的数据格式是python专用的，并且不同版本不向后兼容，同时也不能被其他语言识别。
要和其他语言交互，可以使用内置的json包。cPickle是pickle的一个更快的C语言编译版本。
pickle和cPickle相当于java的序列化和反序列化操作。
'''
with open("./5.p",'rb') as f:
    data = pickle.load(f)

print(data)

print('\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])) #join函数--》返回通过指定字符连接序列中元素后生成的新字符串

### channel.html