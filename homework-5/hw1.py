# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

try:
    with open('text_1.txt', "w") as file:
        while True:
            new_str = input("Enter new data or leave empty for exit: ")
            if not new_str:
                break
            file.write(new_str + '\n')
except (IOError, ValueError) as error:
    print(error)

