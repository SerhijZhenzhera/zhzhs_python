'''
Task 1
Imports practice
Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.
'''

pl_1 = {'attack': 10, 'middle': 10, 'defence': 10,
        'keeper': 100, 'left': 1, 'right': 1, 'center': 1}
pl_2 = {'attack': 70, 'middle': 90, 'defence': 100,
        'keeper': 10, 'left': 1.5, 'right': 0.7, 'center': 0.9}
pl_8 = {'attack': 75, 'middle': 100, 'defence': 75,
        'keeper': 10, 'left': 0.7, 'right': 1.5, 'center': 0.9}
pl_9 = {'attack': 75, 'middle': 100, 'defence': 75,
        'keeper': 10, 'left': 0.75, 'right': 0.75, 'center': 1.5}
pl_11 = {'attack': 100, 'middle': 90, 'defence': 70,
         'keeper': 10, 'left': 0.75, 'right': 0.75, 'center': 1.5}


def cf(*args: dict):
    result_list = []
    for arg in args:
        base_strength = arg['attack']
        modifier_strength = arg['center']
        result = base_strength*modifier_strength
        result_list.append(result)
    return result_list


def rd(*args: dict):
    result_list = []
    for arg in args:
        base_strength = arg['defence']
        modifier_strength = arg['right']
        result = base_strength*modifier_strength
        result_list.append(result)
    return result_list


def main(*args):
    print('центрфорварды:', cf(*args))
    print('правые защитники:', rd(*args))


if __name__ == "__main__":
    main(pl_1, pl_2, pl_8, pl_9, pl_11)


'''
---output---
центрфорварды: [10, 63.0, 67.5, 112.5, 150.0]
правые защитники: [10, 70.0, 112.5, 56.25, 52.5]
'''
