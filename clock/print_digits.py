def dig(d, color):
    digline = dict()
    # устанавливаем цвет⬜ 🟦 🟨 🟥
    if color == 1:
        z = '🟥'
    elif color == 2:
        z = '⬜'
    elif color == 3:
        z = '🟨'
    elif color == 4:
        z = '🟦'
        
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
    digline = dict()
    # устанавливаем цвет⬜ 🟦 🟨 🟥
    if color == 1:
        z = '🟥'
    elif color == 2:
        z = '⬜'
    elif color == 3:
        z = '🟨'
    elif color == 4:
        z = '🟦'  

    digline[1] = ('  ')
    digline[2] = ('  ')
    digline[3] = ('  ')
    digline[4] = ('  ')
    digline[5] = (z)
    return digline
    


digit1 = dig(0, 1)
digit2 = dig(8, 2)
sep = separator(1)
digit3 = dig(1, 3)
digit4 = dig(2, 4)
digit5 = dig(3, 1)
digit6 = dig(4, 2)

for i in range (1, 6):
    print(f'{digit1[i]} {digit2[i]} {sep[i]} {digit3[i]} {digit4[i]}\
 {sep[i]} {digit2[i]} {digit2[i]}')


