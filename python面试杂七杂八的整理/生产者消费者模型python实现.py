'''
1）生产者消费者模型的作用：
1、解决阻塞
2、就是解耦，修改生产者，不会影响消费者，反之亦然。
 
2）在生产环境，用生产者消费者模型，就可以解决：
1、处理瞬时并发的请求问题。瞬时的连接数就不会占满。所以服务器就不会挂了。
2、客户端提交一个请求，不用等待处理完毕，可以在页面上做别的事情。
'''


import time,random
import queue,threading #引入队列模块和线程模块
q = queue.Queue()#队列，全局作用，至少覆盖生产者和消费者函数


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

p1 = threading.Thread(target=Producer,args=('A',)) #设置生产线程
c1 = threading.Thread(target=Consumer,args=('B',)) #设置消费线程
c2 = threading.Thread(target=Consumer,args=('C',)) #设置消费线程
p1.start() #开启线程
c1.start() #开启线程
c2.start() #开启线程

'''
当你设计复杂程序的时候，就可以用生产者消费者模型，来松耦合你的代码,也可以减少阻塞。
'''
