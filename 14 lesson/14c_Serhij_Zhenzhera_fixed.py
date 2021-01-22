'''
Task 3. Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
- max_length: 15
- type_: str
- contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.
'''

from functools import wraps

def arg_rules(type_, max_lenght, contains):
    def rules_check(func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                false_list = []
                if not type(arg) == type_:
                    false_list.append('False... Not a string!')
                if len(str(arg)) > max_lenght:
                    false_list.append('False... Too looong!')
                for stop_word in contains:
                    if stop_word in str(arg):
                        false_list.append(f'False... {stop_word} was found!')
                if false_list == []:
                    return func(arg)
                else:
                    return f'{arg} : {false_list}'                        
        return wrapper
    return rules_check   


@arg_rules(str, 15, ['05', '@'])
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'


if __name__ == "__main__":
    print(create_slogan('johndoe05@gmail.com'))
    print(create_slogan('S@SH05'))
    print(create_slogan('Vasja'))
    print(create_slogan(0))
    print(create_slogan('123456789123456789'))


'''
---output---
johndoe05@gmail.com : ['False... Too looong!', 'False... 05 was found!', 'False... @ was found!']
S@SH05 : ['False... 05 was found!', 'False... @ was found!']
Vasja drinks pepsi in his brand new BMW!
0 : ['False... Not a string!']
123456789123456789 : ['False... Too looong!']
'''
