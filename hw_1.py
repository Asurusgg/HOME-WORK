# НОМЕР 1
def count_sum(a=0, b=0):
    print(a + b)
a = int(input('Type the number'))
b = int(input('Type the other number'))
count_sum()
count_sum(a)
count_sum(a, b)

# НОМЕР 2
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

#a = is_even(5)
#print(a)

# НОМЕР 3
def greet(name):
    return "Привет, " + name + "!"


# print(greet("Павел"))

# НОМЕР 4
def max_num():
    go = True
    while go:
        num_list = [int(nums) for nums in input("Введите числа через пробел: ").split()]
        print('Максимальное число:', max(num_list, key=int))
        q = input("Продолжить? (да/нет) ")
        if q == 'нет':
            go = False


# max_num()
# НОМЕР 5
'''import datetime
h = int(input("Как будет выполняться код? (ручной - 0, автоматический - 1): "))
if h == 0:
    year = int(input("Введите свой год для проверки на високосность: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "Високосный год")
            else:
                print(year, "НЕ високосный год")
        else:
            print(year, "НЕ високосный год")
    else:
        print(year, "НЕ високосный год")
elif h == 1:
    year = datetime.date.today().year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "Високосный год")
            else:
                print(year, "НЕ високосный год")
        else:
            print(year, "НЕ високосный год")
    else:
        print(year, "НЕ високосный год")
else:
    print("Вы ввели число больше чем 1 или меньше чем 0")'''

'''while True:

    def get_year():
        year = int(input('Введите год: '))
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print('Год високосный')

        else:
            print('Год не високосный')

    get_year()'''
