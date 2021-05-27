# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

try:
    with open('text_5.txt', "w") as file:
        numbers = input("Enter numbers separated by spaces: ")
        file.write(numbers)
except (IOError, ValueError) as error:
    print(error)

try:
    with open('text_5.txt') as file:
        numbers = [int(number) for number in file.read().split()]
        print(f"Sum of the numbers in the file: {sum(numbers)}")
except (IOError, ValueError) as error:
    print(error)
