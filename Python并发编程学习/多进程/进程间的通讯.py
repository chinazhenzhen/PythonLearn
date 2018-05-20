#总结：多进程之间的通讯与同步问题，大多用到了，Manager、multiprocessing的queue（一定要用这个）
import time
from multiprocessing import Process,Queue,Pipe
#共享全局变量，不适用于多进程，因为进程是数据的完全拷贝
#pool中的进程间通讯需要使用manager中的queue


#管道通讯
def producer(pipe):
    pipe.send("chinazz")
    time.sleep(2)

def consumer(pipe):
    print(pipe.recv())  #类似于queue.get()

if __name__ == "__main__":
    recevie_pipe,send_pipe = Pipe()
    #pipe只能使用于两个进程,但是在两个进程间通讯速度要比pool快

    my_producer = Process(target=producer,args=(send_pipe,))
    my_consumer = Process(target=consumer,args=(recevie_pipe,))

    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()