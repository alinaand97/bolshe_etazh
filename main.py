# Нужно больше этажей

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if (new_floor > self.number_of_floors or new_floor<1):
            print("Такого этажа не существует")
        else :
            for i in range(1, new_floor+1):
                print(i)

    def __str__(self):
        return "Название: "+ self.name.__str__()+ ", кол-во этажей: "+ self.number_of_floors.__str__()


    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return "Название: "+ self.name.__str__()+ ", кол-во этажей: "+ self.number_of_floors.__str__()

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors +=  other
            return "Название: "+ self.name.__str__()+ ", кол-во этажей: "+ self.number_of_floors.__str__()

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = other + self.number_of_floors
            return "Название: "+ self.name.__str__()+ ", кол-во этажей: "+ self.number_of_floors.__str__()


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1.number_of_floors == h2.number_of_floors) # __eq__

h1.number_of_floors = h1.number_of_floors + 10 # __add__
print(h1)
print(h1.number_of_floors == h2.number_of_floors)


h1.number_of_floors += 10 # __ladd__
print(h1)

h2.number_of_floors = 10 + h2.number_of_floors # __radd__
print(h2)

print(h1.number_of_floors > h2.number_of_floors) # __gt__
print(h1.number_of_floors >= h2.number_of_floors) # __ge__
print(h1.number_of_floors < h2.number_of_floors) # __lt__
print(h1.number_of_floors <= h2.number_of_floors) # __le__
print(h1.number_of_floors != h2.number_of_floors) # __ne__