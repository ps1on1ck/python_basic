# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

def my_func():
    total = 0
    is_asking = True
    while is_asking:
        numbers = input("Enter a string of numbers separated by space or Q to exit: ").split()
        current_sum = 0
        for x in numbers:
            if x.lower() == 'q':
                is_asking = False
                break
            elif x.isnumeric():
                current_sum += int(x)
        print(f"Current step summa: {current_sum}")
        total += current_sum
    print(f"Total: {total}")


my_func()
