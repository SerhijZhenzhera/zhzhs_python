'''
Task 2. Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss.
Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
You can refactor the existing code
'''

'''
id_ - is just a random unique integer
'''


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = [self.name + ':']

    def __str__(self):
        return 'Boss({id_}, {name}, {company})'.format(id_=self.id, name=self.name, company=self.company)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss=None):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def get_boos(self, boss):
        self.boss = boss
        boss.workers.append(self)

    def set_boss(self, boss):
        self.boss = boss
        boss.workers.append(self)

    def del_boss(self, boss):
        self.boss = boss
        boss.workers.remove(self)

    def __str__(self):
        return 'Worker({id_}, {name}, {company})'.format(id_=self.id, name=self.name, company=self.company)


if __name__ == "__main__":
    b1 = Boss(0, 'Gustav', 'Beetroot')
    b2 = Boss(1, 'Andreas', 'Beetroot')
    b3 = Boss(2, 'Galina', 'Beetroot')
    w1 = Worker(100, 'Vanja', 'Beetroot')
    w2 = Worker(101, 'Sanja', 'Beetroot')
    w3 = Worker(102, 'Danja', 'Beetroot')
    w1.get_boos(b1)
    w2.get_boos(b2)
    print(*b2.workers)
    w2.set_boss(b1)
    w2.del_boss(b2)
    print(*b1.workers)
    print(*b2.workers)


'''
Andreas: Worker(1, Sanja, Beetroot)
Gustav: Worker(1, Vanja, Beetroot) Worker(1, Sanja, Beetroot)
Andreas:
---output---

'''
