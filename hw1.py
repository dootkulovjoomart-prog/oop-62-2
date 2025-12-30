class Animal:
    def __init__(self, animal_name , family, speed ):
        self.animal_name = animal_name
        self.family = family
        self.speed = speed

    def dog_info(self):
        return f"I am {self.animal_name} and my family is {self.family} and my speed is {self.speed} km/h"
    def wolf_info(self):
        return f"I am {self.animal_name} and my family is {self.family} and my speed is {self.speed} km/h"




dog = Animal('dog', 'Canids' , 48)
wolf = Animal('wolf', 'Canids',60)
print(dog.animal_name)
print(dog.speed)
print(wolf.animal_name)
print(wolf.speed)
print(dog.dog_info())
print(wolf.dog_info())