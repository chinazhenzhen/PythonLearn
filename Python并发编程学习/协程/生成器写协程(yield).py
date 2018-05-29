
def gen_func():
    #1.可以产出值 2.可以接收值（调用方传递进来的值）
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3

# 生成器不只可以产出值，还可以接收值
if __name__ == "__main__":
    gen = gen_func()
    #在调用send发送非none值之前，我们必须启动一次生成器
    url = next(gen)
    print(url)
    html = "chinazz"  #将html的值传入
    gen.send(html) #send方法可以传递值进入生成器内部，同时还可以重启生成器，执行到下一个yield的位置
    # 总结：从第一个yield暂停的地方开始，send（）传入值，并且执行到下一个 yield，也就是说它会返回值 2