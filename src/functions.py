import json


def load_operations():
    """
    Загружает список операций клиента
    """
    with open('operations.json', 'r', encoding='utf8') as file:
        return json.load(file)


def sort_data(operations):
    """
    Принимает неотсортированный список операций клиента
    Выводит список успешеных операций, сортированных по дате
    """
    dict_operation = []
    for element in operations:
        for k, v in element.items():
            if element not in dict_operation and element["state"] == "EXECUTED":
                dict_operation.append(element)

    return sorted(dict_operation, key=lambda data: data['date'], reverse=True)


def date_prettify(date: str) -> str:
    """
    Получает дату из списка
    Выводит преобразованную дату в виде ДД.ММ.ГГГГ
    """
    date_new = date[0:10].split('-')
    date_new = ".".join(ch for ch in reversed(date_new))
    return date_new


def data_prettify(from_data: str) -> str:
    """
    Получает информацию откуда и куда совершен перевод
    Вывод преобразованную информацию в формате:
    номер карты XXXX XX** **** XXXX; номер счета **XXXX
    """
    from_data_split = from_data.split(' ')
    num = from_data_split[-1]
    if from_data_split[0] == 'Счет':
        return f'{from_data_split[0]} **{num[-4:]}'

    if from_data_split[0] == 'Visa':
        return f'{from_data_split[0]} {from_data_split[1]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'

    return f'{from_data_split[0]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'


class OperationInformation:
    """Принимает строку с данными об операции клиента, выводит информацию в обработанном виде"""
    def __init__(self, raw):
        self.raw = raw
        self.date = date_prettify(raw["date"])
        self.description = raw["description"]
        self.amount = raw["operationAmount"]["amount"]
        self.currency_name = raw["operationAmount"]["currency"]["name"]
        self.to_data = data_prettify(raw["to"])

    def get_date_description(self):
        return f"{self.date} {self.description}"

    def get_data1(self, from_data):
        return f"{from_data} -> {self.to_data}"

    def get_data2(self):
        return self.to_data

    def get_operation_amount(self):
        return f"{self.amount} {self.currency_name}"
