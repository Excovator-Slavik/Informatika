# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    # Делаем из сток списки
    list1 = group1.split(delimiter)
    list2 = group2.split(delimiter)
    # Ищем одинаковые в двух списках (пересечение множеств)
    common = set(list1) & set(list2)
    return sorted(list(common)) # Возвращаем отсортированный список
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group,participants_second_group )
print (f"Общие участники: {result}")
# TODO Провеьте работу функции с разделителем отличным от запятой
