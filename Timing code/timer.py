#using the time module
import time

#function example that do output the same results using different syntax
def print_number(num):
    return [str(i) for i in range(num)]

def print_number_2(num):
    return list(map(str, range(num)))

#output time before function
start_time = time.time()
#run function 
print_number(100)

#output time after function
end_time = time.time()

#calculate the time difference
time_elapsed = end_time - start_time
print(time_elapsed)

#output time before function
start_time = time.time()
#run function 
print_number_2(100)

#output time after function
end_time = time.time()

#calculate the time difference
time_elapsed = end_time - start_time
print(time_elapsed)



#using the TIMEIT module
import timeit
#timeit function takes statement and setup as variables 
#timeit.timeit(stmt, setup)

stmt = """
print_number(100)
"""

setup = """
def print_number(num):
    return [str(num) for num in range(n)]
"""

#timeit
total_time = timeit.timeit(stmt, setup)
print(total_time)

stmt = """
print_number(100)
"""

setup = """
def print_number(num):
    return list(map(str, range(num)))
"""

#timeit
total_time = timeit.timeit(stmt, setup)
print(total_time)


    