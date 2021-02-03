'''
Task 1
Imports practice
Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.
'''

from positions import cf as forward_cnt


pl_b_22 = {'attack': 125, 'middle': 90, 'defence': 70,
           'keeper': 10, 'left': 0.75, 'right': 1.5, 'center': 1.4}


if __name__ == "__main__":
    print(forward_cnt(pl_b_22))


'''
---output---
[175.0]
'''
