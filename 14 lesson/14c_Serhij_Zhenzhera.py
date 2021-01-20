'''
Task 3. Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
- max_length: 15
- type_: str
- contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed;
otherwise, return the result.
'''

def arg_rules(func, type_=str, max_length=15, contains=['05', '@']):
    def wrapper(name):
        if not type(name) == str:
            print('False... Not a string!')
        elif len(name) <= 15 and '05' in name and '@' in name:
            print(f'{name} drinks pepsi in his brand new BMW!') # test
            return f'{name} drinks pepsi in his brand new BMW!'
        else:        
            if len(str(name)) > 15:
                print('False... Too looong!')
            if not '05' in name:
                print('False... 05 was not found!')
            if not '@' in name:
                print('False... @ was not found!') 
    return wrapper   


@arg_rules
def create_slogan(name):
    pass


if __name__ == "__main__":
    create_slogan('johndoe05@gmail.com')
    create_slogan('S@SH05')
    create_slogan('Violeta')
    create_slogan(0)
    create_slogan('123456789123456789')


'''
---output---
False... Too looong!
S@SH05 drinks pepsi in his brand new BMW!
False... 05 was not found!
False... @ was not found!
False... Not a string!
False... Too looong!
False... 05 was not found!
False... @ was not found!
'''
