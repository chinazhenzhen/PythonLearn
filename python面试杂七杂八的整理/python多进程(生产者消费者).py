'''
利用多进程解决生产者消费者类问题类似多线程，所使用的模块不一样，其他稍作修改即可
'''
import time,random
from multiprocessing import Queue,Process #引入队列模块和线程模块  多线程 import queue,threading
q = Queue()#队列，全局作用，至少覆盖生产者和消费者函数 区别多线程 q = queue.Queue()


def Producer(name):  #生产者，将待处理XX提取或者生成，存到队列中
    count =0
    while True:
        time.sleep(random.randrange(3))
        if q.qsize()<3:         # 只要盘子里小于3个包子，厨师就开始做包子
            q.put(count)  #入队
            print("Producer %s has produced %s baozi.." %(name,count))
            count += 1

def Consumer(name): # 消费者，使用队列中的生产者所生产的东西
    count =0
    while True:
        time.sleep(random.randrange(4))
        if not q.empty():       # 只要盘子里有包子，顾客就要吃。
            data = q.get()    #出队
            print(data)
            print('Consumer %s has eat %s baozi...' % (name,data))
        else:           # 盘子里没有包子
            print("---no baozi anymore----")
        count+=1

p1 = Process(target=Producer,args=('A',)) #设置生产进程 #区别：p1 = threading.Thread(target=Producer,args=('A',))
c1 = Process(target=Consumer,args=('B',)) #设置消费进程
c2 = Process(target=Consumer,args=('C',)) #设置消费进程
p1.start() #开启进程
c1.start() #开启进程
c2.start() #开启进程
