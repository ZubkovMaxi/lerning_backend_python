def psp(bal: int, index: int, array: list, k: int):
    if bal <= k - index - 2: #условие для добавления (изменения) на открытую скобку
        array[index] = '('
        psp(bal + 1, index + 1, array, k) #рекурсия с учетом изменившихся аргументов
    if bal > 0: #добавляем (изменяем) на закрытую скобку если баланс отличен от 0
        array[index] = ')'
        psp(bal - 1, index + 1, array, k)
    if index == k: #граничный случай. добавляем последнюю скобку.
        if bal == 0:
            return print(''.join(map(str, array)))

k = 2 * int(input('Введите количество ПАР скобок ')) # Желаемое общее количество скобок
bal = 0 # определяем баланс между открытыми и закрытыми скобками
index = 0 # индекс добавляемой скобки
array = [''] * k # создаём пустой список, длиной к

psp(bal=bal, index=index, array=array, k=k) 