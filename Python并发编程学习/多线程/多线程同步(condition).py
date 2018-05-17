import threading
from threading import Condition

# Condition 线程通讯中最复杂的同步锁，条件控制

class XiaoAi(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="小艾")
        self.cond = cond
    def run(self):
        with self.cond:
            self.cond.wait()
            print("{} : 在".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 好啊！".format(self.name))
            self.cond.notify()

class TianMao(threading.Thread):
    def __init__(self,cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}:小艾同学".format(self.name))
            self.cond.notify()  #notify 通知
            self.cond.wait()    #wait 等待

            print("{}:我们来对古诗吧".format(self.name))
            self.cond.notify()
            self.cond.wait()

if __name__ == "__main__":
    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)

    #线程启动顺序很重要
    #在调用with cond  之后才能调用wait或者notify方法  with condition 实质上执行了 acquire 和 release
    #condition有两层锁，一把底层锁会在线程中调用wait方法的时候释放，上面的锁会在每次调用wait的时候分配一把并放入到cond的wait队列中，等待notify方法的唤醒
    xiaoai.start()
    tianmao.start()