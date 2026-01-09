#using single thread
import time
import concurrent.futures

def cpu_heavy_task(n):
    initial=time.perf_counter()
    print("Starting executing with single thread")
    total = 0
    for i in range(n):
        total += i * i
    final=time.perf_counter()
    print(f"Done with execution, The time it took to run this is {round(final-initial, 2)} sec")  
    return total
with concurrent.futures.ThreadPoolExecutor() as executer:
    x=executer.submit(cpu_heavy_task, 100000000)


# x=cpu_heavy_task(1000000000)
print(x)

'''output:
Starting executing with single thread
Done with execution, The time it took to run this is 112.42 sec
333333332833333333500000000'''
# cpu consumption was 11-13%