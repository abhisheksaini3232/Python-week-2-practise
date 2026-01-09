import time
numbers = list(range(100000000))
start = time.time()
result = [x * x for x in numbers]
end = time.time()
print("List execution time:", end - start)


'''output:
List execution time: 15.552160739898682
'''
#cpu usage: 11-12%
#memory usage 3000-4000 MB