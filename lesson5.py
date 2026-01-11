def simple_decarator(func):
    def wrapper():
        print('перед вызовом')
        func()
        print('после  вызова')
    return wrapper
@simple_decarator
def say_hello():
    print('hello')
say_hello()

def greeting_decarator(func):
    def obertka(name):
        print(f'hello {name}')
        func(name)
    return obertka
@greeting_decarator
def greetting(name):
    print(f'how are you {name}')

greetting("Pdidi")

def repeat_decarator(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                func()
        return wrapper
    return decorator
@repeat_decarator(4)
def hello():
    print('hello')
hello()
def class_decarator(cls):
    class NewClass(cls):
        def method(self):
            print ('New method')
    return NewClass
@class_decarator
class OldClass:
        def method(self):
            print('old method')

test_obj = OldClass()

def is_admin_decarator(func):
    def wrapper(user):
        if user.is_role == 'admi':
            func()
        else:
            print('not dostype')

@is_admin_decarator
def ban(user):
    pass
@is_admin_decarator
def delete(user):
    pass
@is_admin_decarator
def nove(user):
    pass        