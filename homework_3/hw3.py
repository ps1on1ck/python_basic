# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(num1, num2, num3):
    """Принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов."""
    return sum([num1, num2, num3]) - min(num1, num2, num3)


print(f"Sum of the largest two arguments: \
{my_func(int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: ')))}")
