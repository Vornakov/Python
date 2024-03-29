"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

file_name = 'data_write.yaml'
# Готовим значения для записи в словарь

# items
first_item = ['computer', 'printer', 'keyboard', 'mouse']
# items_quantity
second_item = 4
# items_price
third_item = {'computer': '200€-1000€',
              'keyboard': '5€-50€',
              'mouse': '4€-7€',
              'printer': '100€-300€'}

# Записываем значения в словарь
data_to_yaml = {'items': first_item,
                'items_quantity': second_item,
                'items_price': third_item}

# Записываем данные из словаря в файл
with open(file_name, 'w', encoding='utf-8') as f_n:
    yaml.dump(data_to_yaml, f_n, allow_unicode=True, default_flow_style=False)

# Загружаем данные из файла для проверки
with open(file_name, encoding='utf-8') as f_n:
    print(f_n.read())