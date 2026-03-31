# TODO Напишите функцию для поиска индекса товара
def find_item_index(products, target):
    # Идём по списку,где получаем индекс (i), и значение (item)
 for i, item in enumerate(products):
    if item == target:
     return i # После первого совпадения возвращаем индекс

 return None # Делаем, если цикл прошел и ничего не нашлось

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)   # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
