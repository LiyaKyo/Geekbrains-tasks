# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt('141.138.90.60', 'GET', '/downloads/product_2')

parsing_list = []
with open('nginx_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        log_line = line.split(' ')
        parsing_list.append((log_line[0], log_line[5].replace('"', ''), log_line[6]))

print(parsing_list)

