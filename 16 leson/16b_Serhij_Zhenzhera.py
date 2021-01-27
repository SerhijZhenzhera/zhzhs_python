'''
Task 2. Create your own implementation of a built-in function range, named in_range(),
which takes three parameters: `start`, `end`, and optional step.
Tips: See the documentation for `range` function
'''

'''
[https://lms.beetroot.academy/myCourses/lesson/ckir494nq67qo07365ipljwtj]
class MyIterator:

    def __init__(self, _start, _end, step=1):
        self.ind = _start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind > self.end:
            raise StopIteration
        val = self.ind
        self.ind += self.step
        return val
'''


def in_range(*args):
    temp = []
    i = 0
    for arg in args:
        if not type(arg) == int:
            text = 'Only numbers!'
            return text
        else:
            temp.append(arg)
            i += 1
    if i < 2:
        text = 'Add the "end" arg, please!'
        return text
    elif i > 3:
        text = 'Two or three args only!'
        return text
    else:
        def in_range_result(start, end, step=1):
            result = []
            while start <= end:
                result.append(start)
                start += step
            return result
        return in_range_result(*temp)


if __name__ == "__main__":
    print(in_range(1, 12))
    print(in_range(1, 12, 3))
    print(in_range(1, 12, 3, 5))
    print(in_range(1, '5'))
    print(in_range(1))


'''
---output---
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[1, 4, 7, 10]
Two or three args only!
Only numbers!
Add the "end" arg, please!
'''
