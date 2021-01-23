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
    def __init__(self, name, books = [], authors = [], books_ammount = 0):
        self.name = name
        self.books_list = books
        self.authors_list = authors
        self.books_amount = books_ammount
    
    # def __repr__(self):
        # return 'Library({name})'.format(name=self.name)

    def __str__(self):
        return 'Library({name})'.format(name=self.name)
       

    def add_new_book(self, book):
        self.books_list.append(book)
        self.books_amount += 1


    def add_new_author(self, author):
        self.authors_list.append(author)


    def group_by_authors(self, author):
        if author in self.authors_list:
            print(f'{author.name} in our library:')
            for book in self.books_list:
                if book.author == author.name:
                    print(book)
        else:
            print('Any books of this author...')


    def group_by_year(self, year):
            print(f'{year} year in our library:')
            for book in self.books_list:
                if book.year == year:
                    print(book)  
        
     
class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
    
    # def __repr__(self):
        # return 'Book({name}, {year}, {author})'.format(name=self.name, year=self.year, author=self.author)

    def __str__(self):
        return 'Book({name}, {year}, {author})'.format(name=self.name, year=self.year, author=self.author)
    
      
class Author:
    def __init__(self, name, full_name, country, birthday, books = []):
        self.name = name
        self.full_name = full_name
        self.country = country
        self.birthday = birthday
        self.books_list = books


    def add_new_book(self, book):
        self.books_list.append(book)

    # def __repr__(self):
        # return 'Author({full_name}, {country}, {birthday})'.format(full_name=self.full_name, country=self.country, birthday=self.birthday)

    def __str__(self):
        return 'Author({full_name}, {country}, {birthday})'.format(full_name=self.full_name, country=self.country, birthday=self.birthday)



if __name__ == "__main__":
    l1 = Library('Betroot_library')
    print(l1)

    a1 = Author('Лукьяненко', 'Лукьяненко Сергей Васильевич', 'Казахская ССР, Россия', 1968)
    Library.add_new_author(l1, a1)
    print(a1)
    a2 = Author('Васильев', 'Васильев Владимир Николаевич', 'Украина', 1967)
    Library.add_new_author(l1, a2)
    print(a2)
    
    b1 = Book('Ночной Дозор', 1998, 'Лукьяненко')
    print(b1)
    Library.add_new_book(l1, b1)
    Author.add_new_book(a1, b1)

    b2a = Book('Дневной Дозор (соавт.)', 2000, 'Лукьяненко')
    b2b = Book('Дневной Дозор (соавт.)', 2000, 'Васильев')
    print(b2a)
    print(b2b)
    Library.add_new_book(l1, b2a)
    Library.add_new_book(l1, b2b)
    Author.add_new_book(a1, b2a)
    Author.add_new_book(a2, b2b)

    b3 = Book('Сумеречный Дозор', 2003, 'Лукьяненко')
    print(b3)
    Library.add_new_book(l1, b3)
    Author.add_new_book(a1, b3)

    b4 = Book('Лик Черной Пальмиры', 2003, 'Васильев')
    print(b4)
    Library.add_new_book(l1, b4)
    Author.add_new_book(a2, b4)

    b5 = Book('Последний Дозор', 2006, 'Лукьяненко')
    print(b5)
    Library.add_new_book(l1, b5)
    Author.add_new_book(a1, b5)

    b6 = Book('Время инверсий', 2014, 'Васильев')
    print(b6)
    Library.add_new_book(l1, b6)
    Author.add_new_book(a2, b6)

    print(*l1.books_list)
    print(l1.books_amount)
    print(*l1.authors_list)
    print(*a1.books_list)
    print(*a2.books_list)

    Library.group_by_authors(l1, a1)
    Library.group_by_year(l1, 2003)

'''
---output---
Library(Betroot_library)
Author(Лукьяненко Сергей Васильевич, Казахская ССР, Россия, 1968)
Author(Васильев Владимир Николаевич, Украина, 1967)
Book(Ночной Дозор, 1998, Лукьяненко)
Book(Дневной Дозор (соавт.), 2000, Лукьяненко)
Book(Дневной Дозор (соавт.), 2000, Васильев)
Book(Сумеречный Дозор, 2003, Лукьяненко)
Book(Лик Черной Пальмиры, 2003, Васильев)
Book(Последний Дозор, 2006, Лукьяненко)
Book(Время инверсий, 2014, Васильев)
Book(Ночной Дозор, 1998, Лукьяненко) Book(Дневной Дозор (соавт.), 2000, Лукьяненко) Book(Дневной Дозор (соавт.), 2000, Васильев) Book(Сумеречный Дозор, 2003, Лукьяненко) Book(Лик Черной Пальмиры, 2003, Васильев) Book(Последний Дозор, 2006, Лукьяненко) Book(Время инверсий, 2014, Васильев)
7
Author(Лукьяненко Сергей Васильевич, Казахская ССР, Россия, 1968) Author(Васильев Владимир Николаевич, Украина, 1967)
Book(Ночной Дозор, 1998, Лукьяненко) Book(Дневной Дозор (соавт.), 2000, Лукьяненко) Book(Дневной Дозор (соавт.), 2000, Васильев) Book(Сумеречный Дозор, 2003, Лукьяненко) Book(Лик Черной Пальмиры, 2003, Васильев) Book(Последний Дозор, 2006, Лукьяненко) Book(Время инверсий, 2014, Васильев)
Book(Ночной Дозор, 1998, Лукьяненко) Book(Дневной Дозор (соавт.), 2000, Лукьяненко) Book(Дневной Дозор (соавт.), 2000, Васильев) Book(Сумеречный Дозор, 2003, Лукьяненко) Book(Лик Черной Пальмиры, 2003, Васильев) Book(Последний Дозор, 2006, Лукьяненко) Book(Время инверсий, 2014, Васильев)
Лукьяненко in our library:
Book(Ночной Дозор, 1998, Лукьяненко)
Book(Дневной Дозор (соавт.), 2000, Лукьяненко)
Book(Сумеречный Дозор, 2003, Лукьяненко)
Book(Последний Дозор, 2006, Лукьяненко)
2003 year in our library:
Book(Сумеречный Дозор, 2003, Лукьяненко)
Book(Лик Черной Пальмиры, 2003, Васильев)
'''
