
def outer(func):
    def wrapper():
        print('-' * 20)
        func()
        print('-' * 20)
    return wrapper

@outer
def inner():
    print('결과물')

inner()

