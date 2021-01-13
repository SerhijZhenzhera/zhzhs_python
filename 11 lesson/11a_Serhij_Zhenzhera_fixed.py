'''
Task 1. School
Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher. 
'''

class Person:
    def __init__(self, first_name, last_name, height, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.age = age
        self.gender = gender
     
class Student(Person):
    status = __qualname__ # for >= Python 3.3 [https://coderoad.ru/14513019/Python-получить-имя-класса]
    def __init__(self, first_name, last_name, height, age, gender, study, dilig):
        super().__init__(first_name, last_name, height, age, gender)
        self.study = study
        self.diligence = dilig
        
class Teacher(Person):
    status = __qualname__
    def __init__(self, first_name, last_name, height, age, gender, salary, patience):
        super().__init__(first_name, last_name, height, age, gender)
        self.salary = salary
        self.patience = patience


s1 = Student('Aleks', 'Moon', 175, 20, 'androgynous', 90, 75)
t1 = Teacher('Olha', 'Stern', 170, 35, 'woman', 500, 95)
data_list = [s1, t1]

if __name__ == "__main__":
    for card in data_list:
        print(f'''
    ---------------------
    name    | {card.first_name}
    surname | {card.last_name}
    height  | {card.height}
    age     | {card.age}
    gender  | {card.gender}
    status  | {card.status}
    ---------------------
    ''')

'''
---output---
---------------------
    name    | Aleks
    surname | Moon
    height  | 175
    age     | 20
    gender  | androgynous
    status  | Student
    ---------------------


    ---------------------
    name    | Olha
    surname | Stern
    height  | 170
    age     | 35
    gender  | woman
    status  | Teacher
    ---------------------
'''
