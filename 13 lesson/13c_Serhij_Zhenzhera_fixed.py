'''
Task 3. Write a function called `choose_func` which takes a list of nums and 2 callback functions.
If all nums inside the list are positive, execute the first function on that list and return the result of it.
Otherwise, return the result of the second one  
'''

def choose_func(nums, f_1=None, f_2=None):  
    if min(nums) <= 0:
        return remove_negatives(nums)
    else:
        return square_nums(nums)


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def square_nums(nums):
    return [num ** 2 for num in nums]

         
if __name__ == "__main__":
    print(choose_func([1, 2, 3, 4, 5], remove_negatives, square_nums))
    print(choose_func([1, -2, 3, -4, 5], remove_negatives, square_nums))


'''
---output---
[1, 4, 9, 16, 25]
[1, 3, 5]
'''
