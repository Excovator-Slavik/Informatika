numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# Находим пропущенный элемент
missing_index = numbers.index(None)
# Считаем сумму и количество
summa = sum(numbers[:missing_index] + numbers[missing_index+1:])
count = len(numbers)
# Вычисляем среднее и заменяем
numbers[missing_index] = summa / count
# Вычисляем среднее значение
average = summa / count
# Замена пропуска на среднее
numbers[missing_index] = average
print("Измененный список:", numbers)

