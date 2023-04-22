import random
import timeit
import matplotlib.pyplot as plt


list1 = random.sample(range(1, 1000), 10)
x = random.randint(1, 1000)

def generate_list(n):
    return random.sample(range(1,100*n),n)

def linear_search(lst, key):  
    for i in range(len(lst)):  

        if lst[i] == key:  
            return i 
    return -1  

def binary_search(lst, key):
    left, right = 0, len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = lst[middle]
        if key == potentialMatch:
            return middle
        elif key < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1

def fibonacci_search(lst, key):
    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)
    
    n = len(lst)
    fib2, fib1 = 0, 1
    while fib1 < n:
        fib2, fib1 = fib1, fib1 + fib2
    offset = -1
    while fib1 > 1:
        i = min(offset + fib2, n - 1)
        if lst[i] < key:
            fib1, fib2 = fib2, fib1 - fib2
            offset = i
        elif lst[i] > key:
            fib1, fib2 = fib1 - fib2, fib2
        else:
            return i
    if fib1 and offset < n - 1 and lst[offset + 1] == key:
        return offset + 1
    return -1

def calculate_mean_time(func, lst, key):
    times = []
    for i in range(5):
        t = timeit.Timer(lambda: func(lst, key))
        time = t.timeit(number=1)
        times.append(time)
    return sum(times) / len(times)

list_sizes = range(10, 1010, 10)
results = []

for i in range(100):
    for n in list_sizes:
        lst = generate_list(n)
        x = random.randint(1, 100*n)
        linear_time = calculate_mean_time(linear_search, lst, x)
        binary_time = calculate_mean_time(binary_search, lst, x)
        fib_time = calculate_mean_time(fibonacci_search, lst, x)
        results.append((n, linear_time, binary_time, fib_time))
linear_times = []
binary_times = []
fib_times = []

print('================Algorithm_assignment=====================')
print("List Size\tLinear Time\tBinary Time\tFibonacci Time")
for n in list_sizes:
    times = [result[1:] for result in results if result[0] == n]
    linear_time = sum([time[0] for time in times]) / len(times)
    binary_time = sum([time[1] for time in times]) / len(times)
    fib_time = sum([time[2] for time in times]) / len(times)
    linear_times.append(linear_time)
    binary_times.append(binary_time)
    fib_times.append(fib_time)
    print(f"{n}\t\t{linear_time:.6f}\t{binary_time:.6f}\t{fib_time:.6f}")

plt.plot(list_sizes,linear_times,label='Linear Search')
plt.plot(list_sizes,binary_times,label='Binary Search')
plt.plot(list_sizes,fib_times,label='Fibonacci Search')
plt.ylabel('Average exec time')
plt.title('Algorithm assignment')
plt.legend()
plt.show()
# print('==========Algorithm_assignment==============')
# print(f"The list S would be {list1}") 
# print(f"The number is {x}")
# print('')
# print('=====Use Linear_search=====')
# if result1 == -1:  
#     print(f"Number {x} is not in the list1")  
# else:  
#     print(f"Number {x} is in the list1")
# print('')
# print('=====Use binary_search======')
# if result2 == -1:
#     print(f"Number {x} is not in the list1")
# else:
#     print(f"Number {x} is in the list1")
# print('')
# print('=====FibonacciSearch=====')
# if result3 == -1:
#     print(f"Number {x} is not in the list1")
# else:
#     print(f"Number {x} is in the list1")