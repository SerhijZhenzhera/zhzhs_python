'''
Task 2. The birthday greeting program.
Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years” 
'''

name = input('What is your name? ')
age = input('How old are your? ')
if age.isnumeric():
    age_next_year = int(age) + 1
    print('Hello,', name + ', on your next birthday you’ll be', age_next_year, 'years')
else:
    print ('How many?!')        
