"""
Task 1. Run the python interpreter via the terminal. Get familiar with running python commands in the terminal, work with output, etc.
      - Got it!
"""

"""
Task 2. Create a python program named “task2”, and use the built-in function `print` in it several times.
Try to pass “sep”, “end” params and pass several parameters separated by commas.
      - Got it!
Also, provide a comment text above each print statement, mentioned above, with the expected output after execution of the particular print statement.
      - end - необязательный параметр в функции print(), и его значением по умолчанию является \n: "print("x", end='\n') # ends with a new line"
"""

"""
Task 3. Write a program, which has two print statements to print the following text(capital letters “O” and “H”, made from “  # ” symbols)...
Pay attention that usage of spaces is forbidden, as well as creating the whole result text string using “”” ”””, use ‘\n’ and ‘\t’ symbols instead
"""

# Brutal-brief version: x, y, xz = '#'*9, '#\t#', '#'*9 + '\n'; print(x, y, y, y, xz, y, y, x, y, y, sep='\n')

solid_line = '#'*9
two_sides = '#\t#'
solid_line_sep = solid_line + '\n'  # Если все три присваивания в одной строке, то xz не определяется, поскольку сам x должен определиться одновременно с ним - остаётся повторять '#'*9
print(solid_line, two_sides, two_sides, two_sides, solid_line_sep,
      two_sides, two_sides, solid_line, two_sides, two_sides, sep='\n')  # Cогласно условию, строку 25 можно превратить во второй print
