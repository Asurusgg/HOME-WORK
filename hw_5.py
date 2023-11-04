# НОМЕР 1
height = float(input("Введите высоту (в метрах): "))
g = 9.81  # Ускорение свободного падения на Земле
velocity = (2 * g * height) ** 0.5
print(f"Скорость падения: {velocity} м/с")

# НОМЕР 2
class Animal():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def speak(self):
        pass

class Bird(Animal):
    def speak(self):
        return "Чирик-чирик"
    def fly(self):
        return "Я летаю!"

class Lion(Animal):
    def speak(self):
        return "Р-р-р-р-р"

class Monkey(Animal):
    def speak(self):
        return "звуки обезьянки"

bird1 = Bird("Грач", "черный")
print(bird1.speak())
print(bird1.fly())
lion1 = Lion("Африканский лев", "оранжевый")
print(lion1.speak())
monkey1 = Monkey("Шимпадзе", "коричневый")
print(monkey1.speak())


# НОМЕР 3
class Person:
    def __init__(self, name, age, city=None):
        self.name = name
        self.age = age
        self.city = city
    # 5
    def say_hello(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет")
    # 6
    def have_birthday(self):
        self.age += 1
    # 7
    def is_adult(self):
        return self.age >= 18
    # D.1
    def change_city(self, new_city):
        self.city = new_city

person1 = Person("Алиса", 11)
print(f"{person1.name} - {person1.age} лет")
person2 = Person("Боб", 12)
person2.say_hello()
person3 = Person("Карла", 10)
print(f"{person3.name} - {person3.age} лет")
person3.have_birthday()
print(f"{person3.name} - {person3.age} лет")
person4 = Person("Джон", 25)
if person4.is_adult():
    print(f"{person4.name} - взрослый")
else:
    print(f"{person4.name} - несовершеннолетний")

# НОМЕР 4
person5 = Person("Эмили", 14)
person6 = Person("Майк", 22)

people = [person5, person6]

for person in people:
    if person.is_adult():
        print(f"{person.name} - взрослый")
    else:
        print(f"{person.name} - несовершеннолетний")


student2 = Student("Лиза", 16, "Школа №7")
print(student2.say_hello())
