#using single thread
import time

def cpu_heavy_task(n):
    initial=time.perf_counter()
    print("Starting executing with single thread")
    total = 0
    for i in range(n):
        total += i * i
    final=time.perf_counter()
    print(f"Done with execution, The time it took to run this is {round(final-initial, 2)} sec")  
    return total

x=cpu_heavy_task(100000000)
print(x)

'''output:
Starting executing with single thread
Done with execution, The time it took to run this is 112.42 sec
333333332833333333500000000'''
# cpu consumption was 11-13%