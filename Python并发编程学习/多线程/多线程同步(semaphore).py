#Semaphore 是用于控制进入数量的锁(samephone)
#文件读写，写一般允许用一个线程写，读可以允许多个线程读
#在实现线程同步的同时还控制了线程并发的数量
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self,url,sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()

class UrlProducer(threading.Thread):
    def __init__(self,sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20): #开20个线程
            self.sem.acquire()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i),self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)  #控制并发数量，允许3个线程运行
    url_producer = UrlProducer(sem)
    url_producer.start()

#结果是三个三个的并发输出，控制线程数量