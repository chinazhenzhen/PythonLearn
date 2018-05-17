#线程池
#主线程可以获取某个线程的状态或者返回值
#当一个线程完成时，主线程能立即知道
#futures可以让多线程和多进程接口一致

from concurrent.futures import ThreadPoolExecutor,as_completed,wait
import time

def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)  #创建线程池

'''
单个添加
# 通过submit函数提交执行的函数到线程池中，submit是立即返回
task1 = executor.submit(get_html,(3))  #submit在线程池里边加入线程
task2 = executor.submit(get_html,(2))  


#done方法用于判定某个任务是否完成,是非阻塞的方法
print(task1.done()) # false
#result是阻塞的方法，一直等待线程中的任务完成才返回
# result 可以获取task的结果
print(task1.result()) # 3
'''

#批量添加
urls = [3,2,4]
all_tasks = [executor.submit(get_html,(url)) for url in urls]  #get page 2 success get page 3 success get page 4 success

#wait(all_tasks)  wait函数用来阻塞主线程
#print("main")

for futrue in as_completed(all_tasks): #通过as_completed函数获取每个线程运行结束之后的结果
    data = futrue.result()  #data获取的是已经执行玩的线程内的函数的返回值
    print("get {} page success".format(data))

#for data in executor.map(get_html,urls):
#    print("get {} page".format(data))