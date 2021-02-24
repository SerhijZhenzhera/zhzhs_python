'''
Task 1
A bubble sort can be modified to “bubble” in both directions.
The first pass moves “up” the list and the second pass moves “down.”
This alternating pattern continues until no more passes are necessary.
Implement this variation and describe under what circumstances it might be appropriate.
'''


def bubble(nums):
    k = 0
    # l = []
    swapped = True
    while swapped:
        k += 1
        swapped = False
        for i in range(k-1, len(nums) - k):
            # for i in range(len(nums) - 1):
            # l.append(nums[i])
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        for i in range(k-1, len(nums) - k):
            # for i in range(len(nums) - 1):
            # l.append(nums[i])
            if nums[len(nums) - 1 - i] < nums[len(nums) - 1 - i - 1]:
                nums[len(nums) - 1 - i], nums[len(nums) - 1 - i -
                                              1] = nums[len(nums) - 1 - i - 1], nums[len(nums) - 1 - i]
                swapped = True
    # len(l) - без k 42 обращения к элементам списка, с k только 30
    return nums, k,


if __name__ == '__main__':

    print(bubble([19, 2, 31, 45, 6, 11, 121, 27]))


''' 
---output---
([2, 6, 11, 19, 27, 31, 45, 121], 3)
'''
