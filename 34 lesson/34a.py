'''
Task 1
We have the following input list of numbers, some of them are prime.
You need to create a utility function that takes as input a number and returns a bool, whether it is prime or not.
Use ThreadPoolExecutor and ProcessPoolExecutor to create different concurrent implementations for filtering NUMBERS. 
Compare the results and performance of each of them
'''

# [https://tutorialedge.net/python/concurrency/python-processpoolexecutor-tutorial/]
# [https://habr.com/ru/post/229767/]


from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

numbers = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


def task(num):
    pass
    

def ppe():
# executor = ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task)
        task2 = executor.submit(task)
        task3 = executor.submit(task)


def tpe():
# executor = ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(concurrency=3) as executor:
        task



if __name__ == "__main__":
    task(numbers)
    