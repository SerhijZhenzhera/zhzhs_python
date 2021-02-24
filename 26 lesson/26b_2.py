'''
Task 2
Implement the mergeSort function without using the slice operator.
'''


def merge_sort(data):
    part_1 = []
    part_2 = []
    if len(data) > 2:
        g = False
        for el in data:
            if not g:
                part_1.append(el)
                g = True
                continue
            part_2.append(el)
            g = False
        data = part_1 + part_2
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


if __name__ == '__main__':

    print(merge_sort([19, 2, 31, 45, 6, 11, 121, 27]))


'''
---output---
'''
