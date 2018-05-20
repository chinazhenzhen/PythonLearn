
from concurrent.futures import ThreadPoolExecutor,as_completed
from concurrent.futures import ProcessPoolExecutor
import time

# CPU操作使用多进程操作，为什么I/O操作不用多进程，因为进程切换代价要高于线程，I/O操作一般需要不断的切换，是需要不断的进行切换的
#线程间通讯，可以通过全局变量进行通讯，而进程间却不行

#对于耗费cpu的操作，

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)

#cpu操作
'''线程池操作
with ThreadPoolExecutor(3) as excutor:
    all_task = [excutor.submit(fib,(num)) for num in range(25,35)]
    start_time = time.time()
    for future in as_completed(all_task):  # as_completed 获取每个线程执行的结果，整个过程与主线程是阻塞的
        data = future.result()
        print("exe result: {}".format(data))

    print("last time is: {}".format(time.time()-start_time))  #last time is: 2.755469560623169
    
'''
#多进程操作
with ProcessPoolExecutor(3) as excutor:
    all_task = [excutor.submit(fib,(num)) for num in range(25,35)]
    start_time = time.time()
    for future in as_completed(all_task):  # as_completed 获取每个线程执行的结果，整个过程与主线程是阻塞的
        data = future.result()
        print("exe result: {}".format(data))

    print("last time is: {}".format(time.time()-start_time))  #last time is: 1.4141967296600342

