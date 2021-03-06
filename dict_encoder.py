"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и
формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать,
что объём данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import json


user_hobby = {}
with open('users.csv', 'r', encoding='utf-8') as uf:
    with open('hobby.csv', 'r', encoding='utf-8') as hf:
        for uline in uf:
            uline = uline.rstrip()
            hline = hf.readline().rstrip()
            if hline == '':
                hline = 'None'
            user_hobby[uline.replace(',', ' ')] = hline

print(user_hobby, type(user_hobby))

with open('user_hobby.json', 'w', encoding='utf-8') as f:
    json.dump(user_hobby, f)
with open('user_hobby.json', 'r', encoding='utf-8') as f:
    user_hobby2 = json.load(f)
    print(user_hobby2, type(user_hobby2))
