# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


changing_list = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
try:
    with open('text_4.txt') as file:
        for line in file:
            words = line.split(' - ')
            if words[0] in changing_list:
                new_word = changing_list[words[0]]
                new_list.append(new_word + ' - ' + words[1])
            else:
                new_list.append(line)
except (IOError, ValueError) as error:
    print(error)


try:
    with open("text_4_new.txt", "w", encoding="utf-8") as new_file:
        new_file.writelines(new_list)
except (IOError, ValueError) as error:
    print(error)

