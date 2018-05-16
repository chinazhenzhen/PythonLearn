#通过queue的方式 进行线程间的通讯
import time
import threading
from queue import Queue

def get_detail_html(queue):  #消费者
    while True:

        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

def get_detail_url(queue):  # 生产者
    print("get detail url started")
    time.sleep(2)
    for i in range(20):
        queue.put("http://projectsedu.com/{id}".format(id=i))
    print("get detail url end")

if __name__ == "__main__":
    detail_url_queue = Queue(maxsize=1000)

    thread_detail_url = threading.Thread(target=get_detail_url,args=(detail_url_queue,))
    thread_detail_url.start()

    for i in range(10):
        html_thread = threading.Thread(target=get_detail_html,args=(detail_url_queue,))
        html_thread.start()


    #detail_url_queue.task_done()
    #detail_url_queue.join()两个信号量，用来解放或者堵塞


    start_time = time.time()

    print("cast time: {}".format(time.time() - start_time))
