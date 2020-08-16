import datetime

def my_decor(func):
    def wrapper(*args, **kwargs):
        print('Текущее время')
        func(*args, **kwargs)
        print('Такие дела')
    return wrapper


def nowtime(name, age):
    print(datetime.datetime.now())
    print(name)
    print(age)
d = my_decor(nowtime)
d('Олег', 33)

nowtime('Jktu',33)

def no_time(name):
    print('No current time')
    print(name)

n = my_decor(no_time)
n('dude')