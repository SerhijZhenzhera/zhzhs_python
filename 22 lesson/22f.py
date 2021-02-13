'''
Task additional
Replace ints without 'str'-transformation
'''

def sdvig(inval, num = 1):
    len_inval = 0
    inval_test = inval
   
    while inval_test >= 1: # вычисление длины int
       len_inval += 1
       inval_test //= 10

    temp_1 = 10**num # масштаб слепка заготовки для перестановки справа налево <- и масштаб перестановки слева направо ->
    temp_2 = 10**(len_inval-num) # масштаб перестановки справа налево <-
    big_1 = inval // temp_1 # перестановка слева направо ->
    big_2 = big_1 * temp_1 # слепок заготовки для перестановки справа налево <-
    small_1 = inval - big_2 # заготовка для перестановки справа налево <-
    small_2 = small_1 * temp_2 # перестановка справа налево <-
    return small_2 + big_1 # математическое соединение обеих перестановок <+>



if __name__ == '__main__':

    assert sdvig(123) == 312
    assert sdvig(120) == 12
    assert sdvig(120, 2) == 201
    assert sdvig(543210, 3) == 210543
