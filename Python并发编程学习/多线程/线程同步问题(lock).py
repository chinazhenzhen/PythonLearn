from threading import Lock,RLock
import threading

'''
1.用锁会影响性能（要acquire获取锁必须要等待之前acquire获取的锁release释放锁后才能获取）
2.用锁会引起死锁,资源竞争
A(a,b) a,b两个资源,A线程获取
acquire(a)
acquire(b)

B(a,b) a，b两个资源，B线程获取
acquire(b)
acquire(a)
'''
'''
一次  acquire
必须对应一次 release
解决办法:
使用Rlock模块，
可以使用多次 acquire和 release，但是前提是 acquire和release的数量必须是一样的。
'''
total = 0
lock = Lock() #声明锁  lock = RLock 这样可以比较有效的防止因为lock产生的死锁问题

def add(lock):
    global total
    for i in range(1000000):
        lock.acquire()  #获取锁（只有在锁已经释放的条件下，才能获取锁，从而运行下边的代码）
        dosomething(lock)    #这样便产生了死锁
        total += 1
        lock.release()  #释放锁（运行完代码，将获取的锁释放掉）

def dosomething(lock):
    lock.acquire()
    dosomething(lock)
    total += 1
    lock.release()


def desc():
    global lock
    global total
    for i in range(1000000 ):
        lock.acquire()  # 获取锁
        total -= 1
        lock.release()  # 释放锁

t1 = threading.Thread(target=add,args=(lock,))
t2 = threading.Thread(target=desc)

t1.start()
t2.start()

t1.join()
t2.join()

print(total)
