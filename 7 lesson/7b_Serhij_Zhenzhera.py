'''
Task 2. Creating a dictionary.
Create a function called make_country, which takes in a country’s name and capital as parameters.
Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
Make the function print out the values of the dictionary to make sure that it works as intended.
'''

name = input('What is your country name? ')
capital = input("What is the name of it's capital? ")

def make_country(name, capital):
    countries = {'name': name, 'capital': capital}    
    print(countries)

make_country(name, capital)   

'''
---output---
{'name': 'Ukraine', 'capital': 'Kyiv'}
'''
