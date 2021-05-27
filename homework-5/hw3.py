# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.

try:
    with open('text_3.txt', encoding="utf-8") as file:
        employees_list = file.read().split('\n')
        salary_list = []
        employees_less_20_list = []

        for n in employees_list:
            data = n.split()
            salary_list.append(float(data[1]))
            if float(data[1]) < 20000:
                employees_less_20_list.append(data[0])

        average = sum(salary_list) / len(salary_list)
        print(f"List of employees have a salary of less than 20: {employees_less_20_list}, \
average employee income: {average}")
except (IOError, ValueError) as error:
    print(error)

