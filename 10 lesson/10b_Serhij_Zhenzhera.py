'''
Task 2. Doggy age
Create a class Dog with class attribute `age_factor` equals to 7.
Make __init__() which takes values for a dog’s age.
Then create a method `human_age` which returns the dog’s age in human equivalent.
'''


class Dog:
    age_factor = 7

    def __init__(self, d_a):
        self.dog_age = d_a

    def human_age(self):
        return self.dog_age*Dog.age_factor


d1 = Dog(3)
print(d1.human_age())  # test
