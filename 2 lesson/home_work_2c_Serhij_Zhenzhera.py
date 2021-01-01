'''
Task 1. The greeting program. Make a program that has your name and the current day of the week stored as separate variables
and then prints a message like this: “Good day <name>! <day> is a perfect day to learn some python.”
Note that <name> and <day> are predefined variables in source code.
An additional bonus will be to use different string formatting methods for constructing result string.
'''

name = 'Serhij'
week_day = 'Saturday'
print('Good {},'.format('day'), name + '!', week_day, 'is a perfect day to learn some {thing}.'.format(thing = 'PYTHON'))
