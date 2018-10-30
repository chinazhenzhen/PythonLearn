def new_func(func):
    def wrappedfun(username,passwd): #username
        if username == 'root' and passwd == '123456789':
            print('通过认证！')
            print('开始执行附加功能')
            return func(username,passwd)
        else:
            print('用户名或密码错误')
            return
    return wrappedfun

# 带参数的装饰器
#带参数的装饰器，就是在原先的基础上再加一层
def test_new_func(str):
    def new_func(func):
        def wrappedfun(username, passwd):  #func的参数
            if username == 'root' and passwd == '123456789':
                print('通过认证！'+str)
                print('开始执行附加功能')
                return func(username, passwd)
            else:
                print('用户名或密码错误')
                return
        return wrappedfun
    return new_func


@test_new_func("hello")
def orign_1(username, passwd):
    print('开始执行函数')

@new_func
def orign(username, passwd):
    print('开始执行函数')
orign_1('root','123456789')

#
# from functools import wraps
# def outer(func):
#     @wraps(func)
#     def wrapper(a,b):
#         print("before func")
#         print(a)
#         wrapper_result=func(a,b)
#         print("after func")
#         return wrapper_result
#     return wrapper
#
# @outer
# def foo(a,b):
#     return "test"
#
# foo(1, 2)
