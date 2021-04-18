# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    try:
        if x <= 0:
            raise Exception("Вы должны ввести действительное положительное число")
        elif y >= 0:
            raise Exception("Вы должны ввести целое отрицательное число")

        return round(x ** y, 4)
    except Exception as err:
        print(err)


print(my_func(float(input('Введите действительное положительное число: ')),
              int(input('Введите целое отрицательное число: '))))
