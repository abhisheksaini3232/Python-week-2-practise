#using single thread
import time
initial=time.perf_counter()
def cpu_heavy_task(n):
    
    print("Starting executing with single thread")
    total = 0
    for i in range(n):
        total += i * i
    
     
    return total

for _ in range(10):
    cpu_heavy_task(10000000)


final=time.perf_counter()
print(f"Done with execution, The time it took to run this is {round(final-initial, 2)} sec") 
'''output:
Starting executing with single thread
Done with execution, The time it took to run this is 10.12 sec'''
# cpu consumption was 11-13%