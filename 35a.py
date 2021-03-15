'''
Task 1 Practice asynchronous code

Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number.
Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10.
You need to get four lists of results from corresponding functions.

Rewrite the code to use simple functions to get the same results but using a multiprocessing library.
Time the execution of both realizations, explore the results, what realization is more effective,
why did you get a result like this.
'''

import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

task_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# ----- Asynchronous I/O ----- 0.010040044784545898 seconds -----

factorial_asyncio = []
fibonacci_asyncio = []
squares_asyncio = []
cubic_asyncio =[]


async def factorial(name, number):    
    f_ct = 1
    for i in range(2, number+1):
        # await asyncio.sleep(1)
        f_ct *= i
    print(f'Task {name}: factorial({number}) = {f_ct}')
    factorial_asyncio.append(f_ct)


# [https://www.educative.io/edpresso/how-to-implement-the-fibonacci-sequence-in-python]
async def fibonacci(name, number):
    counter = 0
    first = 0
    second = 1
    temp = 0
    while counter <= number:
        # await asyncio.sleep(1) 
        temp = first + second
        first = second
        second = temp
        counter = counter + 1
    print(f'Task {name}: Fibonacci({number}) = {first}')
    fibonacci_asyncio.append(first)


async def squares(name, number):
    # await asyncio.sleep(1)
    sq = number*number
    print(f'Task {name}: squares({number}) = {sq}')
    squares_asyncio.append(sq)


async def cubic(name, number):
    # await asyncio.sleep(1)
    cbc = number*number*number
    print(f'Task {name}: cubic({number}) = {cbc}')
    cubic_asyncio.append(cbc)


async def gather_tasks():
    for t in task_list:
        await asyncio.gather(
            factorial('A', t),
            fibonacci('B', t),
            squares('C', t),
            cubic('D', t),
        )
    print('Factorial asyncio result list:', factorial_asyncio)
    print('Fibonacci asyncio result list:', fibonacci_asyncio)
    print('Squares asyncio result list:', squares_asyncio)
    print('Cubic asyncio result list:', cubic_asyncio)



# ----- simple tasks ----- 0.010036706924438477 seconds -----

def multi_tasks():
    factorial_multi = []
    fibonacci_multi = []
    squares_multi = []
    cubic_multi =[]

    def factorial_m(name, number):    
        f_ct = 1
        for i in range(2, number+1):
            f_ct *= i
        print(f'Task {name}: factorial({number}) = {f_ct}')
        factorial_multi.append(f_ct)

    def fibonacci_m(name, number):
        counter = 0
        first = 0
        second = 1
        temp = 0
        while counter <= number:
            temp = first + second
            first = second
            second = temp
            counter = counter + 1
        print(f'Task {name}: Fibonacci({number}) = {first}')
        fibonacci_multi.append(first)

    def squares_m(name, number):
        sq = number*number
        print(f'Task {name}: squares({number}) = {sq}')
        squares_multi.append(sq)

    def cubic_m(name, number):
        cbc = number*number*number
        print(f'Task {name}: cubic({number}) = {cbc}')
        cubic_multi.append(cbc)

    for t in task_list:
        factorial_m('A', t)
        fibonacci_m('B', t)
        squares_m('C', t)
        cubic_m('D', t)
    print('Factorial multiprocessing result list:', factorial_multi)
    print('Fibonacci multiprocessing result list:', fibonacci_multi)
    print('Squares multiprocessing result list:', squares_multi)
    print('Cubic multiprocessing result list:', cubic_multi)



# ----- Multiprocessing ----- 0.3714609146118164 seconds -----

def multi_process():
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.submit(multi_tasks)




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # result_1 = loop.run_until_complete(factorial('A', 5))
    # result_2 = loop.run_until_complete(fibonacci('B', 5))
    # result_3 = loop.run_until_complete(squares('C', 5))
    # result_4 = loop.run_until_complete(cubic('D', 5))
    
    start_time_5 = time.time()
    result_5 = loop.run_until_complete(gather_tasks())
    print('--- %s seconds ---' % (time.time() - start_time_5))

    start_time_6 = time.time()
    multi_tasks()
    print('--- %s seconds ---' % (time.time() - start_time_6))

    start_time_7 = time.time()
    multi_process()
    print('--- %s seconds ---' % (time.time() - start_time_7))

'''
---output---
Task A: factorial(1) = 1
Task B: Fibonacci(1) = 1
Task C: squares(1) = 1
Task D: cubic(1) = 1
Task A: factorial(2) = 2
Task B: Fibonacci(2) = 2
Task C: squares(2) = 4
Task D: cubic(2) = 8
Task A: factorial(3) = 6
Task B: Fibonacci(3) = 3
Task C: squares(3) = 9
Task D: cubic(3) = 27
Task A: factorial(4) = 24
Task B: Fibonacci(4) = 5
Task C: squares(4) = 16
Task D: cubic(4) = 64
Task A: factorial(5) = 120
Task B: Fibonacci(5) = 8
Task C: squares(5) = 25
Task D: cubic(5) = 125
Task A: factorial(6) = 720
Task B: Fibonacci(6) = 13
Task C: squares(6) = 36
Task D: cubic(6) = 216
Task A: factorial(7) = 5040
Task B: Fibonacci(7) = 21
Task C: squares(7) = 49
Task D: cubic(7) = 343
Task A: factorial(8) = 40320
Task B: Fibonacci(8) = 34
Task C: squares(8) = 64
Task D: cubic(8) = 512
Task A: factorial(9) = 362880
Task B: Fibonacci(9) = 55
Task C: squares(9) = 81
Task D: cubic(9) = 729
Task A: factorial(10) = 3628800
Task B: Fibonacci(10) = 89
Task C: squares(10) = 100
Task D: cubic(10) = 1000
Factorial asyncio result list: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
Fibonacci asyncio result list: [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Squares asyncio result list: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cubic asyncio result list: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
--- 0.010040044784545898 seconds ---
Task A: factorial(1) = 1
Task B: Fibonacci(1) = 1
Task C: squares(1) = 1
Task D: cubic(1) = 1
Task A: factorial(2) = 2
Task B: Fibonacci(2) = 2
Task C: squares(2) = 4
Task D: cubic(2) = 8
Task A: factorial(3) = 6
Task B: Fibonacci(3) = 3
Task C: squares(3) = 9
Task D: cubic(3) = 27
Task A: factorial(4) = 24
Task B: Fibonacci(4) = 5
Task C: squares(4) = 16
Task D: cubic(4) = 64
Task A: factorial(5) = 120
Task B: Fibonacci(5) = 8
Task C: squares(5) = 25
Task D: cubic(5) = 125
Task A: factorial(6) = 720
Task B: Fibonacci(6) = 13
Task C: squares(6) = 36
Task D: cubic(6) = 216
Task A: factorial(7) = 5040
Task B: Fibonacci(7) = 21
Task C: squares(7) = 49
Task D: cubic(7) = 343
Task A: factorial(8) = 40320
Task B: Fibonacci(8) = 34
Task C: squares(8) = 64
Task D: cubic(8) = 512
Task A: factorial(9) = 362880
Task B: Fibonacci(9) = 55
Task C: squares(9) = 81
Task D: cubic(9) = 729
Task A: factorial(10) = 3628800
Task B: Fibonacci(10) = 89
Task C: squares(10) = 100
Task D: cubic(10) = 1000
Factorial multiprocessing result list: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
Fibonacci multiprocessing result list: [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Squares multiprocessing result list: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cubic multiprocessing result list: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
--- 0.010036706924438477 seconds ---
Task A: factorial(1) = 1
Task B: Fibonacci(1) = 1
Task C: squares(1) = 1
Task D: cubic(1) = 1
Task A: factorial(2) = 2
Task B: Fibonacci(2) = 2
Task C: squares(2) = 4
Task D: cubic(2) = 8
Task A: factorial(3) = 6
Task B: Fibonacci(3) = 3
Task C: squares(3) = 9
Task D: cubic(3) = 27
Task A: factorial(4) = 24
Task B: Fibonacci(4) = 5
Task C: squares(4) = 16
Task D: cubic(4) = 64
Task A: factorial(5) = 120
Task B: Fibonacci(5) = 8
Task C: squares(5) = 25
Task D: cubic(5) = 125
Task A: factorial(6) = 720
Task B: Fibonacci(6) = 13
Task C: squares(6) = 36
Task D: cubic(6) = 216
Task A: factorial(7) = 5040
Task B: Fibonacci(7) = 21
Task C: squares(7) = 49
Task D: cubic(7) = 343
Task A: factorial(8) = 40320
Task B: Fibonacci(8) = 34
Task C: squares(8) = 64
Task D: cubic(8) = 512
Task A: factorial(9) = 362880
Task B: Fibonacci(9) = 55
Task C: squares(9) = 81
Task D: cubic(9) = 729
Task A: factorial(10) = 3628800
Task B: Fibonacci(10) = 89
Task C: squares(10) = 100
Task D: cubic(10) = 1000
Factorial multiprocessing result list: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
Fibonacci multiprocessing result list: [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Squares multiprocessing result list: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Cubic multiprocessing result list: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
--- 0.3714609146118164 seconds ---
'''
