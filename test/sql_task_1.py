'''
Task 1 Create a table
Create a table of your choice inside the sample SQLite database, rename it, and add a new column.
Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.
As a solution to this task, create a file named: task1.sql, with all the SQL statements you have used to accomplish this task
'''

# [https://pythonru.com/osnovy/sqlite-v-python]
# [https://www.sqlitetutorial.net/sqlite-alter-table/]

import sqlite3

zvjazok = sqlite3.connect('37_lesson.db')
nakaz = zvjazok.cursor()

nakaz.execute("""CREATE TABLE IF NOT EXISTS trrry(
   a INT PRIMARY KEY,
   b INT,
   c TEXT,
   d VARCHAR(25));
""")
zvjazok.commit()


# ----- COLUMNS and ROWS -----

nakaz.execute(
    """INSERT INTO trrry(a, b, c, d) VALUES(1, 5, 'smile', '-----');""")
zvjazok.commit()

nakaz.execute("ALTER TABLE trrry ADD COLUMN e DEFAULT 0;")
zvjazok.commit()

next_add = [(2, 7, 'super', '-_-', '+'), (3, 9, 'ultra', '___', '*')]

nakaz.executemany(
    """INSERT INTO trrry VALUES(?, ?, ?, ?, ?);""", next_add)
zvjazok.commit()

nakaz.execute("ALTER TABLE trrry RENAME TO sproba;")
zvjazok.commit()


# ----- PRINT -----

nakaz.execute("SELECT * FROM sproba;")
one_result = nakaz.fetchone()
for _ in one_result:
    print('---1---', _)

nakaz.execute("SELECT * FROM sproba;")
one_result = nakaz.fetchone()
print('---2---', one_result)

nakaz.execute("SELECT b FROM sproba;")
one_result = nakaz.fetchone()
print('---3---', one_result)

nakaz.execute("SELECT * FROM sproba;")
two_results = nakaz.fetchmany(2)
print('---4---', two_results)

nakaz.execute("SELECT b FROM sproba;")
two_results = nakaz.fetchmany(2)
print('---5---', two_results)

nakaz.execute("SELECT * FROM sproba;")
all_results = nakaz.fetchall()
print('---6---', all_results)

nakaz.execute("SELECT b FROM sproba;")
all_results = nakaz.fetchall()
print('---7---', all_results)


# ----- UPDATE and DELETE -----

nakaz.execute("SELECT d, e FROM sproba;")
all_results = nakaz.fetchall()
print('---8---', all_results)

nakaz.execute("UPDATE sproba SET d = '!!!' WHERE d = '___';")
zvjazok.commit()

nakaz.execute("SELECT d FROM sproba;")
all_results = nakaz.fetchall()
print('---9---', all_results)

nakaz.execute("DELETE FROM sproba WHERE e = '+';")
zvjazok.commit()

nakaz.execute("SELECT * FROM sproba;")
all_results = nakaz.fetchall()
print('---10---', all_results)


'''
---output---
---1--- 1
---1--- 5
---1--- smile
---1--- -----
---1--- 0
---2--- (1, 5, 'smile', '-----', 0)
---3--- (5,)
---4--- [(1, 5, 'smile', '-----', 0), (2, 7, 'super', '-_-', '+')]
---5--- [(5,), (7,)]
---6--- [(1, 5, 'smile', '-----', 0), (2, 7, 'super', '-_-', '+'), (3, 9, 'ultra', '___', '*')]
---7--- [(5,), (7,), (9,)]
---8--- [('-----', 0), ('-_-', '+'), ('___', '*')]
---9--- [('-----',), ('-_-',), ('!!!',)]
---10--- [(1, 5, 'smile', '-----', 0), (3, 9, 'ultra', '!!!', '*')]
'''
