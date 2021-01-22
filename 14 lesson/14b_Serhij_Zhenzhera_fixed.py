'''
Task 2. Write a decorator that takes a list of stop words and replaces them with * inside the decorated function2
'''

from functools import wraps

def stop_words(stop_list):
    def words_check(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            info = func(*args, **kwargs)
            for word in stop_list:
                info = info.replace(word, '*')
            return info
        return wrapper
    return words_check


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    print(f'I want to print: {name} drinks pepsi in his brand new BMW!')
    print("Let's try:")
    return f'{name} drinks pepsi in his brand new BMW!'


if __name__ == "__main__":
    print(create_slogan('Steve'))


'''
---output---
I want to print: Steve drinks pepsi in his brand new BMW!
Let's try:
Steve drinks * in his brand new *!
'''
