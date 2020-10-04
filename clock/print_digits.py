# Модуль print_digits содержит:  
# 
# Функция dig() - библиотеку цифр 0 - 9
# аргументы: d - цифра(0 - 9).
# возвращает словарь digline из 6 элементов - строк
# 
# Функция separator1 - возвращает 6 строк, 5 первых состоят
# из пробелов, 6 строка содержит точку каждый четный вызов  
# пробел каждый нечетный.
#
# Функция col() генерирует цвет в зависимости от аргумента 
# 1- 🟥, 2 - ⬜, 3 - 🟨, 4 - 🟦, 5 - 🟩.

def col(i):
    if i == 1:
        z = '🟥'
    elif i == 2:
        z = '⬜'
    elif i == 3:
        z = '🟨'
    elif i == 4:
        z = '🟦'  
    elif i == 5:
        z = '🟩'
    return z

def dig(d, color):
    digline = dict()
    z = col(color)
    #генерируем строки цифры нужного цвета
    if d == 0:
        digline[1] = (z + z + z)
        digline[2] = (z + '  ' + z)
        digline[3] = (z + '  ' + z)
        digline[4] = (z + '  ' + z)
        digline[5] = (z + z + z)
    if d == 1:
        digline[1] = (z + z + '  ')
        digline[2] = ('  ' + z + '  ')
        digline[3] = ('  ' + z + '  ')
        digline[4] = ('  ' + z + '  ')
        digline[5] = (z + z + z)
    if d == 2:
        digline[1] = (z + z + z)
        digline[2] = ('    ' + z)
        digline[3] = (z + z + z)
        digline[4] = (z + '    ')
        digline[5] = (z + z + z)
    if d == 3:
        digline[1] = (z + z + z)
        digline[2] = ('    ' + z)
        digline[3] = (z + z + z)
        digline[4] = ('    ' + z)
        digline[5] = (z + z + z)
    if d == 4:
        digline[1] = (z + '  ' + z)
        digline[2] = (z + '  ' + z)
        digline[3] = (z + z + z)
        digline[4] = ('    ' + z)
        digline[5] = ('    ' + z)
    if d == 5:
        digline[1] = (z + z + z)
        digline[2] = (z + '    ')
        digline[3] = (z + z + z)
        digline[4] = ('    ' + z)
        digline[5] = (z + z + z)
    if d == 6:
        digline[1] = (z + z + z)
        digline[2] = (z + '    ')
        digline[3] = (z + z + z)
        digline[4] = (z + '  ' + z)
        digline[5] = (z + z + z)
    if d == 7:
        digline[1] = (z + z + z)
        digline[2] = ('    ' + z)
        digline[3] = ('    ' + z)
        digline[4] = ('    ' + z)
        digline[5] = ('    ' + z)
    if d == 8:
        digline[1] = (z + z + z)
        digline[2] = (z + '  ' + z)
        digline[3] = (z + z + z)
        digline[4] = (z + '  ' + z)
        digline[5] = (z + z + z)
    if d == 9:
        digline[1] = (z + z + z)
        digline[2] = (z + '  ' + z)
        digline[3] = (z + z + z)
        digline[4] = ('    ' + z)
        digline[5] = (z + z + z)
    #возвращаем значение функции в виде словаря
    return (digline)

def separator(color):    
    counter = 0
    digline = dict()
    z = col(color)
    while True:
        digline[1] = ('  ')
        digline[2] = ('  ')
        digline[3] = ('  ')
        digline[4] = ('  ')
        if counter % 2 == 0:
            digline[5] = (z)
        else: 
            digline[5] = ('  ')
        yield digline
        counter += 1
