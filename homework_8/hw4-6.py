# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте
# параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddWarehouseError(WarehouseError):
    def __init__(self, text):
        self.text = f"\033[31mUnable to add the item to the warehouse:\n {text}"


class TransferToDivisionError(Exception):
    def __init__(self, text):
        self.text = text


class OnlyNumericError(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self):
        self.__warehouseList = {'printer': {}, 'scanner': {}, 'xerox': {}}

    def __str__(self):
        return f"{self.__warehouseList}"

    def add_equipment(self, item, quantity):
        if not isinstance(item, OfficeEquipment):
            raise AddWarehouseError(f"\033[31m{item} not office equipment")
        elif type(quantity) != int:
            raise OnlyNumericError("\033[31mPlease enter only digits for quantity parameter")
        else:
            if isinstance(item, Printer):
                model = self.__warehouseList['printer'].get(item.model)
                if model:
                    self.__warehouseList['printer'][item.model] = {'item': item,
                                                                   'quantity': model['quantity'] + quantity}
                else:
                    self.__warehouseList['printer'][item.model] = {'item': item, 'quantity': quantity}
            elif isinstance(item, Scanner):
                model = self.__warehouseList['scanner'].get(item.model)
                if model:
                    self.__warehouseList['scanner'][item.model] = {'item': item,
                                                                   'quantity': model['quantity'] + quantity}
                else:
                    self.__warehouseList['scanner'][item.model] = {'item': item, 'quantity': quantity}
            elif isinstance(item, Xerox):
                model = self.__warehouseList['xerox'].get(item.model)
                if model:
                    self.__warehouseList['xerox'][item.model] = {'item': item,
                                                                 'quantity': model['quantity'] + quantity}
                else:
                    self.__warehouseList['xerox'][item.model] = {'item': item, 'quantity': quantity}

    def transfer_to_division(self, warehouse_type, model, quantity, department):
        current_type = self.__warehouseList.get(warehouse_type)
        if not current_type:
            raise TransferToDivisionError(f"\033[31mInvalid type '{warehouse_type}'")
        elif not current_type.get(model):
            raise TransferToDivisionError(f"\033[31mInvalid model '{model}' in type '{warehouse_type}'")
        elif type(quantity) != int:
            raise OnlyNumericError("\033[31mPlease enter only digits for quantity parameter")

        curr_model = current_type.get(model)
        if curr_model['quantity'] < quantity:
            raise TransferToDivisionError(f"\033[31mNot enough '{model}' on the warehouse")
        elif curr_model['quantity'] == quantity:
            print(f"Quantity of {quantity} {model} transferred to {department} department")
            del self.__warehouseList[warehouse_type][model]
        else:
            self.__warehouseList[warehouse_type][model]['quantity'] = curr_model['quantity'] - quantity
            print(f"Quantity of {quantity} {model} transferred to {department} department")


class OfficeEquipment:
    def __init__(self, model, color):
        self.color = color
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(*args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(*args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__(*args)


storage = Warehouse()
storage.add_equipment(Printer('Printer_1', 'Black'), 5)
storage.add_equipment(Printer('Printer_1', 'Black'), 15)
storage.add_equipment(Printer('Printer_2', 'Black'), 7)
storage.add_equipment(Scanner('Scanner', 'Black'), 4)
storage.add_equipment(Xerox('Xerox', 'Black'), 6)
print('storage before transfer', storage)
storage.transfer_to_division('printer', 'Printer_1', 5, 'CH-1')
storage.transfer_to_division('printer', 'Printer_1', 6, 'CH-1')
storage.transfer_to_division('xerox', 'Xerox', 4, 'CH-1')
print('storage after transfer', storage)

try:
    storage.add_equipment(Printer('Printer_1', 'Black'), '5')
except (WarehouseError, OnlyNumericError, TransferToDivisionError) as err:
    print(err)

try:
    storage.transfer_to_division('printer', 'Printer_7', '3', 'CH-1')
except (WarehouseError, OnlyNumericError, TransferToDivisionError) as err:
    print(err)
