#import print_digits
import time
import datetime
def get_current_time():
    hour = int(datetime.datetime.now().strftime('%H'))
    minute = int(datetime.datetime.now().strftime('%M'))
    second = int(datetime.datetime.now().strftime('%S'))
    return hour, minute, second

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def sleep(period):
    pass

if __name__ == '__main__':
    while True:
        print(get_current_time())
        #  print_digits(current_time)
        time.sleep(10)
        clear_screen()
        break

