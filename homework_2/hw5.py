# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У
# пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них. Подсказка. Например,
# набор натуральных чисел: 7, 5, 3, 3, 2. Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2. Пользователь ввёл
# число 8. Результат: 8, 7, 5, 3, 3, 2. Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1. Набор натуральных
# чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [7, 5, 3, 3, 2]
val = input("Enter a number for rating or enter Q for quit: ")
while val != 'Q':
    if val == 'Q':
        break
    val = int(val)
    if len(rating) == 0:
        rating.append(val)
    else:
        count = rating.count(val)
        if rating[0] < val:
            rating.insert(0, val)
        elif rating[-1] > val:
            rating.append(val)
        else:
            for i, el in enumerate(rating):
                if el == val:
                    if count > 1:
                        if i > 0 and rating[i + 1] < val:
                            rating.insert(i + 1, val)
                            break
                    else:
                        rating.insert(i + 1, val)
                        break
                elif el > val > rating[i + 1]:
                    rating.insert(i + 1, val)
    val = input("Enter a number for rating or enter Q for quit: ")
print('Rating:', rating)
