# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    """Возвращает частное от деления."""
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Error: Division of {a} by zero.")


print(f"Result of division: {division(int(input('Enter first number: ')), int(input('Enter second number: ')))}")
