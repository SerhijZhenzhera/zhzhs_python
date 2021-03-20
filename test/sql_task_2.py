'''
Task 1 Select queries
Use the sample SQLite database hr.db
As a solution to HW, create a file named: task2.sql with all SQL queries:
    write a query to display the names (first_name, last_name) using alias name "First Name", "Last Name" from the table of employees;
    write a query to get the unique department ID from the employee table
    write a query to get all employee details from the employee table ordered by first name, descending
    write a query to get the names (first_name, last_name), salary, PF of all the employees (PF is calculated as 12% of salary)
    write a query to get the maximum and minimum salary from the employees table
    write a query to get a monthly salary (round 2 decimal places) of each and every employee
'''

# [https://stackoverflow.com/questions/82875/how-to-list-the-tables-in-a-sqlite-database-file-that-was-opened-with-attach]
# [https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27]

import sqlite3


def query_general(path):
    zvjazok = sqlite3.connect(path)
    nakaz = zvjazok.cursor()
    nakaz.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    all_results = nakaz.fetchall()
    print(path, 'full tables list ->', all_results)
    try:
        table_tuple = all_results[0]
        table = table_tuple[0]
        print('___Details for path ---', path, '---')
        print('______Table for check:', table)
        nakaz.execute("SELECT * FROM " + table + " ;")
        all_results = nakaz.fetchall()
        print("_________Table '" + table + "' contains:", all_results)
    except:
        IndexError


if __name__ == "__main__":

    path_1 = "C:\\Users\\Regina\\Desktop\\17-20 results\\37\\hr.db"
    path_2 = "C:\\Users\\Regina\\Desktop\\17-20 results\\37\\37_lesson.db"

    query_general(path_1)
    query_general(path_2)


'''
---output---
C:\Users\Regina\Desktop\17-20 results\37\hr.db full tables list -> []
C:\Users\Regina\Desktop\17-20 results\37\37_lesson.db full tables list -> [('sproba',)]
___Details for path --- C:\Users\Regina\Desktop\17-20 results\37\37_lesson.db ---
______Table for check: sproba
_________Table 'sproba' contains: [(1, 5, 'smile', '-----', 0), (3, 9, 'ultra', '!!!', '*')]
'''
