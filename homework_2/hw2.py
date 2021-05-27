# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов
# нужно использовать функцию input().

original_list = []
val = input("Enter a value for list or enter Q for quit: ")
while val != 'Q':
    if val == 'Q':
        break
    original_list.append(val)
    val = input("Enter a value for list or enter Q for quit: ")

custom_list = original_list.copy()

for el in range(1, len(custom_list), 2):
    custom_list[el - 1], custom_list[el] = custom_list[el], custom_list[el - 1]

print(f"Original list: {original_list}. Changed list: {custom_list}")
