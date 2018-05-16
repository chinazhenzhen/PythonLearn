#对于io
import time
import threading

def get_detail_html(url):
    print("get detail html started")
    time.sleep(4)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")

if __name__ == "__main__":
    thread1 = threading.Thread(target=get_detail_html,args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))

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
执行结果：
get detail html started
get detail url started
get detail url end
get detail html end
cast time: 4.000810861587524
'''
