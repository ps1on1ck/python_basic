# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.Функция должна принимать параметры как именованные аргументы.Реализовать вывод
# данных о пользователе одной строкой.

def get_user(first_name, last_name, birthday, city, email, phone):
    return 'First Name: ' + first_name + ', Last name: ' + last_name + ', Birthday: ' + birthday + ', City: ' + city + \
           ', Email: ' + email + ', Phone: ' + phone


result = get_user(first_name="Alphonso", last_name="Kuvalis", birthday="2011-12-01",
                  city="Valencia", email="bode.gwendolyn@example.net", phone="726-450-6778")

print(result)
