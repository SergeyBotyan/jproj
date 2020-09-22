creds = {'name1': 'pass1', 'name2': 'pass2'}

def auth_required(func):
    def proov(*args, **kwargs):
        log = input('Введите логин: ')
        cred_pas = creds.get(log, "No user")
        pas = input('Введите пароль: ')
        if pas != cred_pas:
            return 'Authentication required'
        value = func(*args, **kwargs)
        return value
    return proov

a = int(input('a='))
b = int(input('b='))

@auth_required
def some_func(a, b):
    return(a + b)

print(some_func(a, b))