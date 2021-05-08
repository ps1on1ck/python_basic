# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не
# фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
# команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран. Подсказка: для
# этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем очередного
# элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class OnlyNumericError(Exception):
    def __init__(self, text):
        self.text = text


class NumberList:
    def __init__(self, init_list):
        self._custom_list = init_list

    def __str__(self):
        return self._custom_list

    def start_fill_list(self):
        while True:
            try:
                new_str = input("Enter new number or leave empty for exit: ")
                if not new_str:
                    print(self._custom_list)
                    break
                elif not new_str.isnumeric():
                    raise OnlyNumericError("Please enter only digits")
                self._custom_list.append(int(new_str))
            except OnlyNumericError as err:
                print(err)


one_list = NumberList([])
one_list.start_fill_list()
