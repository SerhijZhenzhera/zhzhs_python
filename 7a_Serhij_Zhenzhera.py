'''
Task 1. A simple function. Create a simple function called favorite_movie,
which takes a string containing the name of your favorite movie.
The function should then print “My favorite movie is named {name}”.
'''

def favorite_movie(movie_name):
    print('My favorite movie is named "' + movie_name + '"')

movie_name = input('What is your favorite movie? ')   
favorite_movie(movie_name)    

'''
---output---
My favorite movie is named "Star Wars"
'''
