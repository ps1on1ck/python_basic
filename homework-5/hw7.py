# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

result = []
try:
    with open('text_7.txt', encoding="utf-8") as file:
        lines = file.read().split('\n')
        firm_list = {}
        average_profit_list = []
        for line in lines:
            if not line:
                break
            words = [words for words in line.split()]
            earn, spend = words[2:]
            total_count = int(earn) - int(spend)
            firm_list[words[0]] = total_count
            if total_count >= 0:
                average_profit_list.append(total_count)

        result.append(firm_list)
        result.append({'average_profit': sum(average_profit_list) / len(average_profit_list)})
except (IOError, ValueError) as error:
    print(error)

try:
    with open('text_7.json', 'w', encoding='utf8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)
except (IOError, ValueError) as error:
    print(error)
