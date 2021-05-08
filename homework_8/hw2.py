# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyOwnError(Exception):
    def __init__(self, text):
        self.text = text


try:
    dividend, divisor = input("Enter the dividend and divisor separated by a space: ").split()
    dividend = int(dividend)
    divisor = int(divisor)
    if divisor == 0:
        raise MyOwnError('Please enter a divisor less or more than 0')
    print(dividend/divisor)
except (ValueError, MyOwnError) as err:
    print(err)

