# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.

while True:
    month_index = int(input("Введите месяц в виде целого числа от 1 до 12:"))
    if 0 < month_index <= 12:
        dict_seasons = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
        list_season = []

        for value in dict_seasons.values():
            list_season.append(value)

        season_index = 1
        if month_index <= 2 or month_index == 12:
            season_index = 1
        elif 3 <= month_index <= 5:
            season_index = 2
        elif 6 <= month_index <= 8:
            season_index = 3
        elif 9 <= month_index <= 11:
            season_index = 4
        else:
            season_index = 4

        print(f'Месяц c номером {month_index} относится к времени года: {list_season[season_index - 1]}')
        print(f'Месяц c номером {month_index} относится к времени года: {dict_seasons.get(season_index)}')
        break
