# НОМЕР 2
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True

    def stop_engine(self):
        self.engine_started = False


class Sedan(Car):
    def start_engine(self):
        self.engine_started = False


class SUV(Car):
    def start_engine(self):
        self.engine_started = True


sedan = Sedan("Toyota", "Camry")
suv = SUV("Jeep", "Cherokee")

sedan.start_engine()
suv.stop_engine()

print(f"{sedan.make} {sedan.model}: Двигатель {'запущен' if sedan.engine_started else 'остановлен'}")
print(f"{suv.make} {suv.model}: Двигатель {'запущен' if suv.engine_started else 'остановлен'}")


# НОМЕР 3
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        pass


class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

    def display_info(self):
        return f"Книга: {self.name}, Автор: {self.author}, Цена: {self.price} руб."


class Toy(Product):
    def __init__(self, name, price, category):
        super().__init__(name, price)
        self.category = category

    def display_info(self):
        return f"Игрушка: {self.name}, Категория: {self.category}, Цена: {self.price} руб."


book = Book("Гарри Поттер", 500, "Джоан Роулинг")
toy = Toy("Лего", 30, "Конструктор")

print(book.display_info())
print(toy.display_info())


