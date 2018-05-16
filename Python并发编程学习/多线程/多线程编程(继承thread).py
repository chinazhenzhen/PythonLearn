'''
跟直接调用Thread类用法一样，这里只不过继承了这个类，进行了一定程度的修改和定制
'''
import time
import threading

class GetDetailHtml(threading.Thread):
    def __init__(self,name): #重载，继承__init__函数
        super().__init__(name=name)

    def run(self):  #重写run函数，继承threading,Thread类，run函数即多线程执行的函数
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self,name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == "__main__":
    thread1 = GetDetailHtml("get html")
    thread2 = GetDetailUrl("get url")

    # 当主线程退出的时候，子线程kill掉
    #thread1.setDaemon(True)  #将thread1设置为守护线程，当主线程结束的时候，子线程也会义无反顾的结束自己的生命
    #thread2.setDaemon(True)

    start_time = time.time()
    thread1.start()
    thread2.start()

    #主线程被子线程阻塞，主线程会在这个地方等待子线程执行完成。
    #如果不写join，主线程会提前完成相应的任务
    thread1.join()
    thread2.join()

    print("cast time: {}".format(time.time() - start_time))

'''
运行结果：
get detail html started
get detail url started
get detail html end
get detail url end
cast time: 4.0044920444488525
'''