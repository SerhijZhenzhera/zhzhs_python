'''
Task 1
A shared counter
Make a class called Counter, and make it a subclass of the Thread class in the Threading module.
Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000.
Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times)
and for each time increments the value of the counter by 1.
Create 2 instances of the thread and start them, then join them and check the result of the counter, it should be 200.000, right?
Run it a couple of times and consider some different reasons why you get the answer that you get.
'''

# [https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews/xlm6QznGGNE]

from threading import Thread


class Counter(Thread):

    def __init__(self):
        self.counter = 0
        self.rounds = 100000

    def run(self):
        for _ in range(self.rounds):
            self.counter += 1


if __name__ == "__main__":

    count_1 = Counter()
    thread_1 = Thread(target=count_1.run)
    thread_1.start()
    print('Первый поток:', count_1.counter)
    thread_2 = Thread(target=count_1.run)
    thread_2.start()
    print('Второй поток:', count_1.counter)
    thread_1.join()
    thread_2.join()
    print('С главным потоком:', count_1.counter)

    print('---------------------')

    count_2 = Counter()
    thread_3 = Thread(target=count_2.run)
    thread_3.start()
    print('Первый поток:', count_2.counter)
    thread_3.join()
    thread_4 = Thread(target=count_2.run)
    thread_4.start()
    print('Второй поток:', count_2.counter)
    thread_4.join()
    print('С главным потоком:', count_2.counter)

'''
---output---

-----e.i. 10.000 times-----
Первый поток: 10000
Второй поток: 20000
С главным потоком: 20000
---------------------
Первый поток: 10000
Второй поток: 20000
С главным потоком: 20000

-----e.i. 100.000 times-----
Первый поток: 17715
Второй поток: 65112
С главным потоком: 149385
---------------------
Первый поток: 11724
Второй поток: 109853
С главным потоком: 200000 # остаётся единственный постоянный результат
'''
