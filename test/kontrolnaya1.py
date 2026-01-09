class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f'{self.name} ready for battle'

class MageHero(Hero):
    def __init__(self, name, lvl, hp , mp ):
        super(MageHero, self).__init__(name, lvl, hp)
        self.mp = mp



    def action(self):
        return f'Mage {self.name} casts a spell! Mp: {self.mp}'


class WarriorHero(MageHero):
    def __init__(self, name , lvl , hp, mp):
        super(WarriorHero, self).__init__(name, lvl , hp, mp)

    def action(self):
        return f'Warrior {self.name} chops with a sword . Level:{self.lvl}'



class BankAccount():
    bank_name = 'O bank'
    def __init__(self,  hero, balance ,password , bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name


    def login(self , password):
        if password == self.__password:
            return True
        else:
            return False
    @property
    def full_info(self):
        return f'Name :{self.hero} / Balance :{self._balance} '

    def get_bank_name(self):
        return f'Name bank:{self.bank_name}'
    def bonus_for_level(self):
        return f'bonus_for_level: {self.hero.lvl * 10}'

    def __str__(self):
        return f"{self.hero.name} | Balance: {self._balance}"

    def __add__(self, other):
        if type(self.hero) != type(other.hero):
            return self._balance + other._balance
        else:
            return 'You cannot add'


    def __eq__(self, other):
        if  self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl:
              return True
        else:
            return False




from abc import ABC, abstractmethod
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(SmsService):
    def send_otp(self, phone):
        return f'<text>cod: 1234</text><phone>{phone}</phone>'

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}

hero = Hero('John' , 100 , 500)
magehero = MageHero('robert' , 99 , 500,60 )
warriorhero = WarriorHero('zhoomart', 89 , 1000,50 )
acc1 = BankAccount(hero, 3456 , 'qwer', 'o bank')
acc2 = BankAccount(magehero, 6532, 'asd', 'o bank')
acc3 = BankAccount(warriorhero, 4536, 'zxc', 'o bank')

print(hero.action())
print(magehero.action())
print(warriorhero.action())
print(acc1)
print(acc2)
print(acc3)

print("\n=== Examination __add__ ===")
print("The sum of the bills of two magicians:", acc1 + acc2)
try:
    print("sum:", acc1 + acc2)
except TypeError as e:
    print('Error:',e)



print("\n=== Examination __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

sms = KGSms()
print("\n", sms.send_otp (+996503848516))

