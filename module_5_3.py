class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        title = str (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return title
    def __eq__(self,other):
        return self.number_of_floors==other.number_of_floors
    def __lt__(self,other):
        return self.number_of_floors<other.number_of_floors
    def __le__(self,other):
        return self.number_of_floors<=other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors>other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors>=other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        return self.number_of_floors + value
    def __radd__(self, value):
        return self.__add__(value)

house = House('ЖК Эльбрус', 30)


house.go_to(10)
house.go_to(37)


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Альпы', 15)

print(h1)
print(h2)
print(len(h1))
print((len(h2)))
print(h1==h2)
print(h1<h2)
print(h1<=h2)
print(h1>h2)
print(h1>=h2)
print(h1!=h2)
h1 += 10 # __iadd__

print(h1)



h2 = 10 + h2 # __radd__

print(h2)

