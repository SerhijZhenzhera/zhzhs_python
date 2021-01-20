'''
Task 2. Write a decorator that takes a list of stop words and replaces them with * inside the decorated function2
'''

def stop_words(func, words = ['pepsi', 'BMW']):
    def wrapper(name):
        print(f'{name} drinks {words[0]} in his brand new {words[1]}!') # test
        return f'{name} drinks {words[0]} in his brand new {words[1]}!'
    return wrapper


@stop_words
def create_slogan(name):
    pass


if __name__ == "__main__":
    create_slogan('Steve')


'''
---output---
Steve drinks pepsi in his brand new BMW!
'''
