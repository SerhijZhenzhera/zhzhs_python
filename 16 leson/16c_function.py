'''
Task 3. Create your own implementation of an iterable, which could be used inside for-in loop.
Also, add logic for retrieving elements using square brackets syntax.
'''


def iter_for_in(iterable):
    try:
        sproba = len(iterable)
    except:
        TypeError
        sproba = 'Non-iterable!'
        return sproba
    result = []
    i = 0  
    while True:
        if i < len(iterable):
            result.append(iterable[i])
            i += 1
        else:
            return result
    return result


'''
[https://apirobot.me/posts/iterables-iterators-generators-in-python]
import re
class Finder:
    def __init__(self, pattern, text):
        self.text = text
        self.matches = re.findall(pattern, text)
    def __iter__(self):
        return FinderIterator(self.matches)
class FinderIterator:
    def __init__(self, matches):
        self.matches = matches
        self.index = 0
    def __next__(self):
        try:
            match = self.matches[self.index]
        except IndexError:
            raise StopIteration()
        self.index = self.index + 1
        return match
'''


if __name__ == "__main__":
    print(iter_for_in(['a', 'b', 'c', 'd', 'e']))
    print(iter_for_in(('a', 'b', 'c', 'd', 'e')))
    print(iter_for_in('abcde'))
    print(iter_for_in(12345))
    print(iter_for_in(None))



'''
---output---
['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'd', 'e']
Non-iterable!
Non-iterable!
'''
