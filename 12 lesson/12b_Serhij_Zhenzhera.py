'''
Task 2. Library
Write a class structure that implements a library. Classes:
    1) Library - name, books = [], authors = []
    2) Book - name, year, author (author must be an instance of Author class)
    3) Author - name, country, birthday, books = []
Library class
Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class
and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books 
'''

class Library:
    library_books_list = []
    def __init__(self, name, books, authors):
        self.name = name
        self.books_list = books
        self.authors_list = authors
    
    def __repr__(self):
        return 'Library({name}, {books}, {authors})'.format(name=self.name, books=self.books, authors=self.authors)

    def __str__(self):
        return 'Library({name}, {books}, {authors})'.format(name=self.name, books=self.books, authors=self.authors)

    def new_book(name, year, *author):
        Book.name = name
        Book.year = year
        Book.author = author
        Author.author = author
        Book.books_amount += 1
        n_book = []
        n_book.append(Book.name)
        n_book.append(Book.year)
        n_book.append(Book.author)
        Library.library_books_list.append(n_book)
        Library.books = Library.library_books_list

        
    def group_by_authors(author):
        Author.author = author
        print(author)
        for book in Library.library_books_list:
            for element in book:
                if author in str(element):
                    print(book)
       

    def group_by_year(year):
        Book.year = year
        print(year)
        for book in Library.library_books_list:
            for element in book:
                if str(year) in str(element):
                    print(book)


     
class Book:
    books_amount = 0
    def __init__(self, name, year, *author):
        self.name = name
        self.year = year
        self.author = author
    
    def __repr__(self):
        return 'Book({name}, {year}, {author})'.format(name=self.name, year=self.year, author=self.author)

    def __str__(self):
        return 'Book({name}, {year}, {author})'.format(name=self.name, year=self.year, author=self.author)
    
      
class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books_list = books

    def __repr__(self):
        return 'Author({name}, {country}, {birthday}, {books})'.format(name=self.name, country=self.country, birthday=self.birthday, books=self.books)

    def __str__(self):
        return 'Author({name}, {country}, {birthday}, {books})'.format(name=self.name, country=self.country, birthday=self.birthday, books=self.books)







if __name__ == "__main__":
    b1 = Library.new_book('Дневной Дозор', 2000, 'Лукьяненко', 'Васильев')
    print('автор(авторы):', *Book.author, '-:- название:', Book.name, '-:- год издания:', Book.year)
    b2 = Library.new_book('Ночной Дозор', 1998, 'Лукьяненко')
    print('автор(авторы):', *Book.author, '-:- название:', Book.name, '-:- год издания:', Book.year)
    print(Book.books_amount)
    print(Library.library_books_list)
    print(Library.books)
    Library.group_by_authors('Лукьяненко')
    Library.group_by_authors('Васильев')
    Library.group_by_year(2000)

'''
---output---
автор(авторы): Лукьяненко Васильев -:- название: Дневной Дозор -:- год издания: 2000
автор(авторы): Лукьяненко -:- название: Ночной Дозор -:- год издания: 1998
2
[['Дневной Дозор', 2000, ('Лукьяненко', 'Васильев')], ['Ночной Дозор', 1998, ('Лукьяненко',)]]
[['Дневной Дозор', 2000, ('Лукьяненко', 'Васильев')], ['Ночной Дозор', 1998, ('Лукьяненко',)]]
Лукьяненко
['Дневной Дозор', 2000, ('Лукьяненко', 'Васильев')]
['Ночной Дозор', 1998, ('Лукьяненко',)]
Васильев
['Дневной Дозор', 2000, ('Лукьяненко', 'Васильев')]
2000
['Дневной Дозор', 2000, ('Лукьяненко', 'Васильев')]
'''
