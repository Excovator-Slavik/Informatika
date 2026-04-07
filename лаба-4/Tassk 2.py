# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    #Открываем файл для чтения
    with open(INPUT_FILENAME, mode ='r', encoding="utf-8")as f:
        #Созаём объём DictReader, который возващает строки в OrderDict
        reader = csv.DictReader(f)
        #Превращаем итератор в список.
        # при записи в JSON он превратился в обычный словать {}
        data = list(reader)
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, mode='w', encoding = "utf-8") as json_f:
        json.dump(data, json_f, indent=4, ensure_ascii= False)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
