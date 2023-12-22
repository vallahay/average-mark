marks = input().split() # Вводим оценки

total_sum = 0 # сумма оценок(value)
number_of_marks = 0 # количество оценок(counter)

for mark in marks:
    if mark[-1] == 'k':  # Если оценка за контрольную
        mark_value = int(mark[:-1])  # Убираем 'k' и преобразуем в целое число
        total_sum += mark_value * 2  # Учитываем как две оценки
        number_of_marks += 2  # Увеличиваем счётчик количества оценок на 2
    elif mark[-1] == 's':  # Если оценка за самостоятельную работу
        mark_value = int(mark[:-1])  # Убираем 's' и преобразуем в целое число
        total_sum += mark_value * 1.5  # Умножаем на 1.5
        number_of_marks += 1.5  # Увеличиваем счётчик количества оценок на 1
    else:
        mark_value = int(mark)  # Преобразуем в целое число
        total_sum += mark_value  # Добавляем оценку как обычное значение
        number_of_marks += 1  # Увеличиваем счётчик количества оценок на 1

average_mark = total_sum / number_of_marks  # Считаем средний балл

print(average_mark)