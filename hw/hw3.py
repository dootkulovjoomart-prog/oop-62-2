class User:
    def __init__(self, name , _email, __password):
        self.name = name
        self.email = _email
        self.__password = __password


    def show_email(self):
        return self.email
    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

    def change_password(self, new_password, old_password):
        if self. __password == old_password:
            self.__password = new_password
            return 'Password changed'
        else:
            return 'Password not chenged'



user = User('John', 'john.email', 12345 )
print(user.change_password('<PASSWORD>' , 12345 ))

print(user.name)
print(user.show_email())
print(user.check_password('<PASSWORD>'))

from abc import ABC, abstractmethod
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def move(self):
        return 'The car is driving along the road'
class Bicycle(Transport):
    def move(self):
        return 'Tру bicycle is riding on a bike path'




car = Car()
bike = Bicycle()
print(car.move())
print(bike.move())
