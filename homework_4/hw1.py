# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    name, production_in_hours, rate_per_hour, bonus = argv

    def employee_payroll(a, b, c):
        try:
            return (int(a) * int(b)) + int(c)
        except ValueError as value_err:
            print(f'Error: {value_err}')


    result = employee_payroll(production_in_hours, rate_per_hour, bonus)
    if result:
        print(f'Заработноя плата сотрудника: {result}')

except ValueError as err:
    print(f'Error: {err}')
