# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subjects = {}
try:
    with open('text_6.txt', encoding="utf-8") as file:
        lines = [line for line in file.read().replace('(пр)', '').replace('(л)', '').replace('(лаб)', '').split('\n')]
        for line in lines:
            if not line:
                break
            new_list = line.replace('-', '').split(':')
            numbers = [int(number) for number in new_list[1].split()]
            subjects[new_list[0]] = sum(numbers)
        print(subjects)
except (IOError, ValueError) as error:
    print(error)
