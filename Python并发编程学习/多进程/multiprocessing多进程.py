#multiprocess的用法跟threading的用法基本一直
import multiprocessing
import time

def get_html(n):
    print(n)
    time.sleep(n)
    return n



progree = multiprocessing.Process(target=get_html,args=(2,))
print(progree.pid) #None
progree.start()
print(progree.pid) #17142
progree.join()
print("main end")

pool = multiprocessing.Pool(multiprocessing.cpu_count())
result = pool.apply_async(get_html,args=(3,))

pool.close()
pool.join()
print(result.get())
