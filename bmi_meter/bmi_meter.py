#практика
print('Практика')
a = int(input('Первое '))
b = int(input('Второе '))
c = int(input('Третье '))
#1 неудачный
print(str(not(a and b and c)) or 'Нет нулевых значений')
#2
print(a or b or c or 'Введены все нули')
#3
print(a - b - c if a > b + c else 'Условие не выполнено')
#4
print(b + c - a if a <= b + c else 'Условие не выполнено')
#5
if a > 50 and (b > a or c > a):
    print('Вася')
#6
if a > 5 and b == 7 and c == 7:
    print('Петя')


# BMI метр
d = dict()
l = list()
while True:
    #Ввод и перевод роста в метры
    mass = int(input('Введите вашу массу тела в килограммах: '))
    h = int(input('Введите ваш рост в сантиметрах: '))
    age = int(input('Введите ваш возраст (число полных лет): '))
    gender = str(input('Введите ваш пол (м или ж): '))
    #проверяем на корректность пол
    while True:
        if gender != 'м' and gender != 'ж':
            gender = str(input('Вводите только м или ж,'\
            'третьего не дано: '))
        else:
            break
    name = (input('Введите ваше имя: '))
    h = h / 100

    # формула ИМТ
    bmi = round(mass / (h * h), 1) 
    #Вывод ИМТ текстом
    print('Ваш индекс массы тела: ', bmi)

    #Вывод ИМТ графически 
    if bmi >=20 and bmi <=50: 
        print('20' + '=' * int(bmi - 20) + '|' + '=' * int(50 - bmi) + '50')
    elif bmi < 20:
        print(int(bmi), '|' + '=' * int(50 - bmi) + '50')
    else:
        print('20' + '=' * int(bmi - 20) + '|', int(bmi))
    #даем рекомендации
    if age < 15:
        print('В вашем возрасте за ИМТ можно не следить.')
    elif age > 70 and bmi  > 35:
        print('Внимательнее следите за своим рационом!')
    elif gender == 'ж' and bmi < 10 or gender == 'м' and bmi > 50:
        print('Вызывайте скорую, ваша жизнь в опасности!')
    else:
        print('У вас все в порядке.')
        
    l = (mass, h, age, gender)
    d[name] = (l)
    print('Список пользователей:')
    for i in d.keys():
        print(i)
    
    #операции
    operation = 'zero'
    while operation != 'n':
        operation = input('Если хотите удалить пользователя, введите d \n'\
        'Для вывода данных пользователя введите u \n'\
        'Для выхода введите q \n'\
        'Для ввода нового ползователя введите n \n')
        if operation == 'd':
            delete = input('Введите имя пользователя для удаления ')
            del(d[delete])
            print('Запись с именем ' + delete + ' удалена.')
            print('Список пользователей:')
            for i in d.keys():
                print(i)
        elif operation == 'u':
            user = input('Какого пользователя показать? ')
            print(d[user])
        elif operation == 'q':
            break
        elif operation == 'n':
            break
        else:
            continue
    if operation == 'q':
            break    
print('Спасибо за работу!')