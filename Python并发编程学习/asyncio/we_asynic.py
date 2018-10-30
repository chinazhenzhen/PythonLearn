import asyncio
import time


now = lambda: time.time()


async def do_some_work(x):
    print("waiting:", x)

start = now()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop() # 创建事件loop
task = loop.create_task(coroutine) # 创建task
print(task)
loop.run_until_complete(task)
print(task)
print("Time:",now()-start)