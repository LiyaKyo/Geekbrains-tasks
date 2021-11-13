# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера (?).

parsing_list = []
parsing_set = set()
with open('nginx_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        log_line = line.split(' ')
        parsing_list.append(log_line[0])
        parsing_set.add(log_line[0])

max_count, spamer_ip = 0, ''
for el in parsing_set:
    count = parsing_list.count(el)
    if count > max_count:
        max_count = count
        spamer_ip = el

print(spamer_ip, max_count)