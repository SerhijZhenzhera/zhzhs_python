'''
Task 1. Files.
Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents. Run your two scripts from the system command line. 
    - Does the new file show up in the directory where you ran your scripts? 
    - What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings;
add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.
'''

# -----1----- файл появился C:\Users\Regina\myfile.txt
task_9_1 = open('myfile.txt', 'w')
task_9_1.write('\n Hello \n\n')
task_9_1.close()
task_9_1 = open('myfile.txt', 'a')
task_9_1.write(' file \n\n world!')
task_9_1.close()

# -----2----- не надо вызывать метод close, закрытие происходит автоматически
with open('myfile.txt', 'r') as task_9_1:
    print(task_9_1.read())

'''
---output---

 Hello

 file

 world!

'''
