# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
# строк и сохраните в переменные, выведите на экран.

var_1 = 5
var_2 = 'str'
print(var_1)
print(var_2)
name = input('Please enter your name:')
age = input('Please enter your age:')
print('My name is ' + name + '. I`m ' + age + ' years old.')
var_number = int(input("Enter an integer number:"))
print('integer number', var_number)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

minutesInHour = 60
secondsInHour = 3600
time = int(input("Введите время в секундах:"))

hours = time // secondsInHour
minutes = time % secondsInHour // minutesInHour
seconds = time % secondsInHour % minutesInHour
print(f"Время в формате чч:мм:сс {hours:02d}:{minutes:02d}:{seconds:02d}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

n = input('Введите число: ')
sum_numbers = int(n) + int(n + n) + int(n + n + n)
print(f'Сумма чисел {n} + {n}{n} + {n}{n}{n}: {sum_numbers}')


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

val = int(input("Введите целое положительное число:"))
result = val % 10
while val >= 1:
    val = val // 10
    if val % 10 > result:
        result = val % 10

print("Самая большая цифра в числе:", result)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее
# сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Введите значение выручки фирмы:'))
cost = int(input('Введите значение издержек фирмы:'))

if revenue > cost:
    profit = revenue / cost
    print("Фирма работает с прибылью. Рентабельность выручки: %.2f" % profit)
    employees = int(input("Введите численность сотрудников фирмы:"))
    profit_per_employee = profit / employees
    print("Прибыль фирмы в расчете на одного сотрудника составляет: %.2f" % profit_per_employee)
elif revenue == cost:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток. Убыток фирмы: %.2f" % (cost - revenue))


# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня. Например: a = 2, b = 3. Результат: 1-й день: 2 2-й день: 2,2 3-й день:
# 2,42 4-й день: 2,66 5-й день: 2,93 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input("Введите результат пробежки первого дня: "))
b = int(input("Введите желаемый результат: "))
result = 1
while a < b:
    a += (a * 0.1)
    result += 1

print("Результат будет достигнут на {} день".format(result))
