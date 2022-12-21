def largest_numer (numbers: str) -> str:
    # Подготавливаем входные данные под нужный тип. Обязательно испуользуем 'str'
    # с 'int' дальнейшая сортировка работать не будет
    numbers_list_str = [str(number) for number in numbers.split()]
    len_number_list = len(numbers_list_str)# длина списка
    for a in range (1, len_number_list): # сортируем список из str значений пузырьковой сортировкой по убыванию.(numbers_list_str.sort(key=str, reverse=True))
        for k in range(0, len_number_list - a): 
            if numbers_list_str[k] < numbers_list_str[k + 1]:
                numbers_list_str[k], numbers_list_str[k + 1] = numbers_list_str[k + 1], numbers_list_str[k]
    # "склеиваем" то что получилось и выводим в нужном формате
    return ''.join(map(str, numbers_list_str))

numbers = input('Введите набор чисел, разделяя их пробелами ')
print(largest_numer(numbers=numbers))