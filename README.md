# Решение задач, в рамках обучения ООО "Автоматика-сервис", на языке python
------
## Спринт 1 :white_check_mark:
<details>
<summary> Ближайщий ноль 
<a href="https://github.com/ZubkovMaxi/lerning_backend_python/blob/main/nearest.py">(nearest.py)</a>
</summary>
<p>Алгоритм решения задачи:</p>
<p>1.Получаем на входе список с указанием номеров домов и пустых участков</p>
<p>2.Первичная обработка входных данных. Определение количества участков</p>
<p>3.Определение количества участков до пустого участка слева от текущего, для каждого участка слева направо#если первый участок не пустой, принимаем максимально возможное количество участков</p>
<p>4.Аналогично п.3 определяем количество до пустого участка справа, для каждого участка справа налево </p>
<p>5.Определяем минимальные расстояния до пустого участка для каждого участка из двух полученных списков</p>
<p>6.Выводим искомое значение в нужном формате</p>
</details>
<details>
<summary> Ловкость рук
<a href="https://github.com/ZubkovMaxi/lerning_backend_python/blob/main/sleght_of_hand.py">(sleght_of_hand.py)</a>
</summary>
<p>Алгоритм решения задачи:</p>
<p>1.Получаем на входе возможное количество нажатых клавиш игроками</p>
<p>2.Принимаем первичное количество очков = 0</p>
<p>3.Создаём "пустой" список для расчёта возможных нажатых клавиш, без учета ограничений по п.1. Индекс соответствует цифре</p>
<p>4.Принимаем на вход 4 строки с цифрами и "." </p>
<p>5.Для каждой цифры, входящей в строки, увеличиваем количество возможных нажатых клавиш в списоке п.3, соответственно индексу</p>
<p>6.Считаем итоговые очки исходя из ограничений п.1 и выводим количество очков</p>
</details>

-----
## Спринт 2 :white_check_mark:
<details>
<summary> Правильные скобочные последовательности
<a href="https://github.com/ZubkovMaxi/lerning_backend_python/blob/main/psp.py">(psp.py)</a>
</summary>
<p>Алгоритм решения задачи:</p>
<p>1.Получаем на входе количество скобок</p>
<p>2.Создаём переменные необходимых аргументов функции, пустой список.</p>
<p>3.Определяем условия для рекуррентных и граничного случаев и условия вывода на печать.</p>
<p>4. При переходе на следующий уровень рекурсии, изменяем аргументы функции в зависимости какую скобку записали, передаём изменненый список.</p>
<p>5.При наступлении граничного случая (список заполнился, баланс = 0) выводим на печать.
<p>6.Возвращаемся на верхний уровень рекурсии
</details>
<details>
<summary> Составить самое большое число
<a href="https://github.com/ZubkovMaxi/lerning_backend_python/blob/main/largest_numer.py">(largest_numer.py)</a>
</summary>
<p>Алгоритм решения задачи:</p>
<p>1.Получаем на входе числа.</p>
<p>2.Первичная обработка входных данных. Формируем список. Для дальнейшей сортировки важно использовать 'str' значения. Чтоб значение '9' было 'выше' '89'</p>
<p>3.Сортируем список в порядке убывания.</p>
<p>4.'Склеиваем' итоговый список в строку. Выводим результат</p>
</details>


-----
## Спринт 3 :black_square_button: