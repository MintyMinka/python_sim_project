from random import randint

class Character:
    def __init__(self, name:str, family, age:int, hunger=10, energy=10, hygene=10, inteligence=10, strenght=10, creativity=10):
        self.name = name
        self.age = age
        if self.age<7:
            raise ValueError("Postać musi mieć minimum 7 lat!")
        self.family = family
        self.family.add_member(self)
        self.hunger = hunger
        self.energy = energy
        self.hygene = hygene
        self.inteligence = inteligence
        self.strenght = strenght
        self.creativity = creativity
    def get_needs(self):
        return f"najedzenie: {self.hunger}, energia: {self.energy}, higiena: {self.hygene}"
    
    def get_skills(self):
        return f"inteligencja: {self.inteligence}, siła: {self.strenght}, kreatywność: {self.creativity}"

    def is_child(self):
        if self.age < 18:
            return True

    def is_adult(self):
        if self.age < 60 and self.age >= 18:
            return True
    
    def is_elder(self):
        if self.age >= 60:
            return True
    
    def add_age(self):
        self.age += 1
        return f"{self.name} ma teraz {self.age} lat! Wszystkiego najlepszego!"
    
    def change_hunger(self, n:int):
        if self.hunger + n < 0:
            raise ValueError(f"{self.name} potrzebuje coś zjeść, zanim wykona to zadanie!")
        elif self.hunger + n > 10:
            self.hunger = 10
        else:
            self.hunger += n

    def change_energy(self, n:int):
        if self.energy + n < 0:
            raise ValueError(f"{self.name} potrzebuje odpocząć, zanim wykona to zadanie!")
        elif self.energy + n > 10:
            self.energy = 10
        else:
            self.energy += n

    def change_hygene(self, n:int):
        if self.hygene + n < 0:
            raise ValueError(f"{self.name} potrzebuje skorzystać z łazienki, zanim wykona to zadanie!")
        elif self.hygene + n > 10:
            self.hygene = 10
        else:
            self.hygene += n
    
    def change_needs(self, hunger:int, energy:int, hygene:int):
        self.change_hunger(hunger)
        self.change_energy(energy)
        self.change_hygene(hygene)
    
    def change_inteligence(self, n: int):
        if self.inteligence + n < 0:
            self.inteligence = 0
        else:
            self.inteligence += n

    def change_strenght(self, n: int):
        if self.strenght + n < 0:
            self.strenght = 0
        else:
            self.strenght += n

    def change_creativity(self, n: int):
        if self.creativity + n < 0:
            self.creativity = 0
        else:
            self.creativity += n
    
    def go_to_work(self):
        if not self.is_adult():
            raise ValueError(f"{self.name} nie jest osobą dorosłą, więc nie może iść do pracy")
        money = self.inteligence + self.creativity + self.strenght
        self.change_needs(-2, -5, -1)
        self.family.change_money(money)
        return f"{self.name} idzie do pracy i zarabia {money} PY"
    
    def go_to_school(self):
        if not self.is_child():
            raise ValueError(f"{self.name} nie jest dzieckiem, więc nie może iść do szkoły")
        self.change_needs(-2, -5, -1)
        self.change_inteligence(3)
        return f"{self.name} idzie do szkoły"
    
    def get_pension(self):
        if not self.is_elder():
            raise ValueError(f"{self.name} nie jest emerytem, więc nie może pobierać emerytury")
        money = (self.inteligence + self.creativity + self.strenght)//2
        self.change_needs(-1, -1, -1)
        self.family.change_money(money)
        return f"{self.name} pobiera emeryturę w wysokości {money} PY"
    
    def exercise(self):
        event = randint(1, 4)
        self.change_needs(-1, -4, -3)
        if event == 1:
            self.change_strenght(4)
            return f"{self.name} idzie pobiegać"
        elif event == 2:
            self.change_strenght(2)
            return f"{self.name} robi pajacyki"
        elif event == 3:
            self.change_strenght(3)
            return f"{self.name} robi przysiady"
        else:
            self.change_strenght(-3)
            return f"{self.name} doznaje kontuzji!"
            
class Family:
    def __init__(self, surname:str, money=1000):
        self.surname = surname
        self.money = money
        self.members = []
    
    def __str__(self):
        return f"rodzina {self.surname}"

    def get_money(self):
        return f"fundusze: {self.money} PY"

    def add_member(self, character:Character):
        self.members.append(character)
    
    def change_money(self, amount:int):
        if self.money + amount < 0:
            raise ValueError(f"Rodzina {self.surname} nie posiada wystarczająco dużo pieniędzy! Ich obecny stan konta to {self.money} PY")
        self.money += amount

class Furniture:
    def __init__(self, size:int, price:int, house):
        self.size = size
        self.price = price
        self.house = house
        self.house.add_furniture(self)

class Fridge(Furniture):
    def __str__(self):
        return 'lodówka'

    def eat(self, person:Character):
        person.change_hunger(5)
        person.family.change_money(-10)
        return f"{person.name} je posiłek"

class Toilet(Furniture):
    def __str__(self):
        return 'toaleta'

    def use_toilet(self, person:Character):
        person.change_hygene(4)
        return f"{person.name} korzysta z toalety"

class Bath(Furniture):
    def __str__(self):
        return 'wanna'

    def take_bath(self, person:Character):
        person.change_hygene(6)
        return f"{person.name} myje się"

class Bookshelf(Furniture):
    def __str__(self):
        return "biblioteczka"

    def read_book(self, person: Character):
        event = randint(1, 4)
        person.change_needs(-1, -2, -1)
        if event == 1:
            person.change_inteligence(5)
            if person.is_child():
                return f"{person.name} czyta podręcznik z matematyki"
            else:
                return f"{person.name} czyta ciekawą książkę popularnonaukową"
        elif event == 2:
            person.change_inteligence(-3)
            if person.is_child():
                return f"{person.name} czyta bardzo nudną i niezrozumiałą lekturę"
            else:
                return f"{person.name} czyta bardzo nudną i niezrozumiałą książkę o filozofii"
        elif event == 3:
            person.change_creativity(5)
            if person.is_child():
                return f"{person.name} czyta książkę fantasy"
            else:
                return f"{person.name} czyta tomik poezji"
        else:
            person.change_creativity(-3)
            if person.is_child():
                return f"{person.name} czyta długą i przewidywalną książkę o problemach nastolatków"
            else:
                return f"{person.name} czyta długi i przewidywalny romans"

class TV(Furniture):
    def __str__(self):
        return "telewizor"

    def watch_tv(self, person: Character):
        event = randint(1, 4)
        person.change_needs(-1, -1, -1)
        if event == 1:
            person.change_inteligence(5)
            if person.is_child():
                return f"{person.name} ogląda program edukacyjny dla dzieci i młodzieży"
            else:
                return f"{person.name} ogląda interesujący film dokumentalny"
        elif event == 2:
            person.change_inteligence(-3)
            if person.is_child():
                return f"{person.name} ogląda niezbyt mądre kreskówki"
            else:
                return f"{person.name} ogląda kontrowersyjne reality show"
        elif event == 3:
            person.change_creativity(5)
            if person.is_child():
                return f"{person.name} ogląda emocjonującą bajkę przygodową"
            else:
                return f"{person.name} ogląda inspirującą biografię słynnego artysty"
        else:
            person.change_creativity(-3)
            if person.is_child():
                return f"{person.name} ogląda nieciekawy serial dla dzieci i młodzieży"
            else:
                return f"{person.name} ogląda nudną konferencję prasową"

class Bed(Furniture):
    def __str__(self):
        return "łóżko"

    def sleep(self, char:Character):
        char.change_energy(7)
        return f"{char.name} idzie spać" 

class House:
    def __init__(self, name:str, family:Family, capacity=50, bill_price=500, bills=0):
        self.name = name
        self.family = family
        self.family.house = self
        self.capacity = capacity
        self.bills = bills
        self.bill_price = bill_price
        self.furniture = []

    def __str__(self):
        return f"dom {self.name}"
    
    def get_bills(self):
        return f"rachunki do spłacenia: {self.bills} PY"

    def add_bills(self):
        self.bills += self.bill_price
    
    def pay_bills(self):
        self.family.change_money(-self.bills)
        self.bills = 0
        return f"Rodzina {self.family.surname} spłaca rachunki"

    def add_furniture(self, piece:Furniture):
        if piece.size > self.capacity:
            raise ValueError(f"Ten dom nie ma wystarczająco miejsca na ten przedmiot!")
        self.family.change_money(-piece.price)
        self.furniture.append(piece)
        self.capacity -= piece.size