import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    ...  # TODO считать содержимое csv файла
    data = []

    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
