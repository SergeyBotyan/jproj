
#считаем количество запросов (равно числу строк)
log_file = open('access.log', 'r')

log_file.seek(1)
r_num = 0

while True:
    line = log_file.readline()
    if not line:
        break
    r_num += 1
print('Количество запросов      - ', r_num)

#считаем уникальные IP
log_file.seek(1)
iplist = []
while True:
    line = log_file.readline()
    p_line = line.split(' ')
    iplist.append(p_line[0])
    if not line:
        break
iplist = set(iplist)
print('Количество уникальных IP - ', len(iplist))

#выводим список браузеров (обрабатывал только 100 000 строк)
log_file.seek(1)
browserlist = []
for i in range(1, 100000):
    line = log_file.readline()
    p_line = line.split(' ')
    p_len = len(p_line[-2])
    if p_len > 3 and p_len < 15:
        browserlist.append(p_line[-2])

browserlist = list(set(browserlist))
print('Список браузеров - ', browserlist)

#выводим число запросов для каждого браузера
table = {}
num_calls = 0
for i in browserlist:
    log_file.seek(2)
    for j in range(1, 100000):
        line = log_file.readline()
        p_line = line.split(' ')
        if p_line[-2] == str(i):
            num_calls += 1
    if num_calls > 50:
        table[i] = {num_calls}
    num_calls = 0
print('Частота использования браузеров(фильтр >50)')

for key, value in table.items():
    print(key[:-1], "---", value)

log_file.close()






