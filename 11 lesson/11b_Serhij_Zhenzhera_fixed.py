'''
Task 2. Mathematician
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
    square_nums (takes a list of integers and returns the list of squares)
    remove_positives (takes a list of integers and returns it without positive numbers
    filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'
'''


class Mathematician:
    def __init__(self, num_list):
        self.num_list = num_list
  
    def square_nums(self):
        square_list = []
        for i in range(len(self.num_list)):
            if type(self.num_list[i]) is int:
                square_list.append(int(self.num_list[i])**2)
            else:
                square_list.append('!not int!')
        return square_list
    
    def remove_positives(self):
        negatives_list = []
        for i in range(len(self.num_list)):
            if type(self.num_list[i]) is int and self.num_list[i] < 0:
                negatives_list.append(int(self.num_list[i]))
            else:
                pass
        return negatives_list

    def filter_leaps(self):
        leaps_list = []
        for i in range(len(self.num_list)):
            if not type(self.num_list[i]) is int:
                pass
            elif self.num_list[i] % 4 != 0 or self.num_list[i] % 100 == 0 and self.num_list[i] % 400 != 0:
                pass
            else:
                leaps_list.append(int(self.num_list[i]))
        return leaps_list

m1 = Mathematician([7, 11, 'test', -5, 9])
m2 = Mathematician([-7, 11, 'test', -5, 9])
m3 = Mathematician(['test', 44, 313, 1000, 1234, 1884, 1979])
   

if __name__ == "__main__":
    print(f'SQUARES: {m1.square_nums()}')
    print(f'NEGATIVES: {m2.remove_positives()}')
    print(f'LEAPS: {m3.filter_leaps()}')

'''
---output---
SQUARES: [49, 121, '!not int!', 25, 81]
NEGATIVES: [-7, -5]
LEAPS: [44, 1884]
'''
