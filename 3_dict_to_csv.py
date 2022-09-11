"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

data = [
    {'name': 'Иван', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 15, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    {'name': 'Маша', 'age': 35, 'job': 'Scientist'}, 
    {'name': 'Петя', 'age': 31, 'job': 'Programmer'}, 
    {'name': 'Вова', 'age': 22, 'job': 'Big boss'},
]

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('exports.csv', 'w', encoding='utf-8', newline='') as myfile:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(myfile, fields, delimiter=';')
        writer.writeheader()
        for user in data:
            writer.writerow(user)

if __name__ == "__main__":
    main()
