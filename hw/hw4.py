class Notification:
    def __init__(self,text):
        self.text = text


    def __str__(self):
        return self.text

    def __call__(self):
        return ('Notification sent')

n = Notification('New notification')
print(n)
print(n())

class Vector:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __add__(self , other):
        return Vector(self.x + other.x , self.y + other.y)

    def __eg__(self , other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False



v1 = Vector(2,3)
v2 = Vector(1,1)
v3 = v1 + v2
print(v3.x, v3.y)
print(v1 == v2)

class User:
    def __init__(self , name , role):
        self.name = name
        self.role = role

    @classmethod
    def create_admin(cls,name):
        return cls(name , 'Admin')

admin = User.create_admin('Zhoomart')
print(admin.name)
print(admin.role)