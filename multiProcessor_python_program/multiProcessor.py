#using multiProcessing
import time
import concurrent.futures
initial=time.perf_counter()

def cpu_heavy_task(n):
    print("Starting executing with multiProcessing")
    total = 0
    for i in range(n):
        total += i * i
    return total

with concurrent.futures.ProcessPoolExecutor() as executer:
    time_taken=[executer.submit(cpu_heavy_task, 10000000) for _ in range(10)]


final=time.perf_counter()
print(f"Done with execution, The time it took to run this is {round(final-initial, 2)} sec")



'''output:
Starting executing with multiProcess
Done with execution, The time it took to run this is 0.06 sec'''
# cpu consumption was %