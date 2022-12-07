def nearest(array: str) -> str:
    """Функция определяет расстояние до ближайшего нуля"""

    array_list_int = [int(n) for n in array.split()] #из строки на входе, формируем список с интовыми значениями
    len_array = len(array_list_int)                  #счетаем количество участков
    A_left_to_right = []
    B_right_to_left = []                             
    C_nearet_zero = []                               #резервируем память под три списка
    
    dist = len_array                                 #первоначальное значение дистанции до нуля обозначим максимально большое
    for m in array_list_int:                         #проверяем значение до 0 слева 
        if m == 0:
            dist = 0
        else:
            dist += 1
        A_left_to_right.append(dist)                 #записываем значения для кождого элемента в список

    dist = len_array                                 #Обновляем значение и повторяем действия с конца списка
    for a in reversed(array_list_int):
        if a == 0:
            dist = 0
        else:
            dist += 1
        B_right_to_left.append(dist)
    B_right_to = reversed(B_right_to_left)
    
    for i in range(len_array):                      #из двух списков выбираем минимальное значение соответственно индексу (с учетом что второй список записан в обратном порядке)
        b = min(A_left_to_right[i], B_right_to_left[len_array - 1 - i])
        C_nearet_zero.append(b)
    
    return ' '.join(map(str, C_nearet_zero))

            
print(nearest('0 1 2 77 33 3 0 0 7 0'))

