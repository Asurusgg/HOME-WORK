# НОМЕР 1
class SchoolStudent:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def greeting(self):
        print(f"Привет, я {self.name}, учусь в {self.grade} классе!")

student = SchoolStudent("Иван", 5)
student.greeting()

# НОМЕР 2
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} издает звук: {self.sound}")

dog = Animal("Собака", "Гав-гав!")
cat = Animal("Кошка", "Мяу-мяу!")
dog.make_sound()
cat.make_sound()

# НОМЕР 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")

book = Book("Гарри Поттер", "Джоан Роулинг")
book.display_info()

# НОМЕР 4
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce(self):
        print(f"Этот фрукт - {self.name}, его цвет {self.color}.")

apple = Fruit("Яблоко", "красный")
banana = Fruit("Банан", "желтый")
apple.introduce()
banana.introduce()


player.score_goal()
print(f"{player.name} забил {player.goals} голов.")
