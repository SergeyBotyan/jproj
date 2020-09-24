def my_gen():
    for i in range(1, 7):
        if i % 3 == 0:
            yield 'Василий'
            i += 1
        else:
            yield i
            i += 1

for i in my_gen():
    print(i)