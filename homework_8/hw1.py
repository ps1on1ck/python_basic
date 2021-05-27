# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, full_date):
        self.full_date = full_date
        self.date = self.extract_date(self.full_date)
        self.validate_date(self.date)

    def __str__(self):
        return f"Entered date: {self.full_date}"

    @classmethod
    def extract_date(cls, full_date):
        day, month, year = full_date.split("-")
        day = (int(day) if day.isnumeric() else day)
        month = (int(month) if month.isnumeric() else month)
        year = (int(year) if year.isnumeric() else year)

        if isinstance(day, int) & isinstance(month, int) & isinstance(year, int):
            return day, month, year
        return 'Enter a valid date'

    @staticmethod
    def validate_date(data):
        if isinstance(data, str):
            extract_date = Date.extract_date(data)
            if isinstance(extract_date, str):
                return f"Invalid date format"
            day, month, year = extract_date
        else:
            day, month, year = data

        if not day or not month or not year:
            return f"Invalid date format"
        elif (1 <= day <= 31) and (1 <= month <= 12):
            return f"The date is correct"
        else:
            return f"Invalid date format"


date_1 = Date("3-05-2021")
print(date_1)
print('1', Date.extract_date("asd-05-2021"))
print('2', Date.extract_date("03-05-2021"))
print('3', Date.validate_date("03-05-2021"))
print('4', Date.validate_date("qw-05-2021"))

