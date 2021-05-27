# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

try:
    with open('text_2.txt') as file:
        lines = file.readlines()
        new_line_list = [f'Words in line {index}: {len(line.split())}' for index, line in enumerate(lines, 1)]
        data_lines = '\n'.join(new_line_list)
        print(f"Number of lines: {len(lines)}\n{data_lines}")
except (IOError, ValueError) as error:
    print(error)

