class Hero:
    # конструктор класса
    def __init__(self, name , lvl , hp ):

        # атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f'I am {self.name} base action !!'
#Обьект
kirito = Hero("Ardager", 100, 1000)
tomy = Hero("Tom", 2000, 3000)
print(tomy.lvl)
print(tomy.action()) 