import print_digits
import time
import datetime
# функция get_current_time возвращает три значения
# hour, minute, second текущего времени в формате строк.
def get_current_time():
    hour = datetime.datetime.now().strftime('%H')
    minute = datetime.datetime.now().strftime('%M')
    second = datetime.datetime.now().strftime('%S')
    return hour, minute, second
# функция clear_screen определяет операционую систему и очищает 
# экран терминала
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    
    while True:
        h, m, s = get_current_time()
        h0 = int(h[0])
        h1 = int(h[1])
        m0 = int(m[0])
        m1 = int(m[1])
        s0 = int(s[0])
        s1 = int(s[1])
                   
        if s1 >= 0 and s1 < 2:
            color = 1
        elif s1 >= 2 and s1 < 4:
            color = 2
        elif s1 >= 4 and s1 < 6:
            color = 3
        elif s1 >= 6 and s1 < 8:
            color = 4
        else:
            color = 5
        sep = print_digits.separator(color)
        for i in (1, 2):
            digit1 = print_digits.dig(h0, color)
            digit2 = print_digits.dig(h1, color)
            blink = next(sep)
            digit3 = print_digits.dig(m0, color)
            digit4 = print_digits.dig(m1, color)
            digit5 = print_digits.dig(s0, color)
            digit6 = print_digits.dig(s1, color)
            for i in range (1, 6):
                print(f'{digit1[i]} {digit2[i]} {blink[i]} {digit3[i]}'
                f' {digit4[i]} {blink[i]} {digit5[i]} {digit6[i]}')
            time.sleep(0.5)
            clear_screen()
        

