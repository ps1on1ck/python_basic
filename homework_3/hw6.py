# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
# первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна
# попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную
# ранее функцию int_func().

def int_func(string):
    new_str = []

    for word in string.split():
        if word.isascii():
            new_str.append(word)

    return ' '.join(new_str).title()


print(f"text -> {int_func('text')}")
print(f"ice авп ъghj jапро hjjпаро вапрghgh cool -> {int_func('ice авп ъghj jапро hjjпаро вапрghgh cool')}")
print(int_func(input("Enter string: ")))
