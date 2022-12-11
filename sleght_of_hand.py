def sleght_of_hand(k: int) -> int:
    points = 0
    array = [0] * 10
    for row in range(4):
        for value in input(f'Введите 4 символа {row + 1}-ой строки без пробелов: '):
            if value != '.':
                array[int(value)] += 1
    for index in array:
        points += 1 if 0 < index <= 2 * k else 0
    return points


k = int(input('Ввод количества одновременно нажатых клавиш '))
print(sleght_of_hand(k=k))