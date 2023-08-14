import json

def load_operations():
    """
    Загружает
    """
    with open('operations.json', 'r', encoding='utf8') as file:
        return json.load(file)
def date_prettify(date: str) -> str:
    date_new = date[0:10].split('-')
    date_new = ".".join(ch for ch in reversed(date_new))
    return date_new


def data_prettify(from_data: str) -> str:
    from_data_split = from_data.split(' ')
    num = from_data_split[-1]
    if from_data_split[0] == 'Счет':
        return f'{from_data_split[0]} **{num[-4:]}'

    if from_data_split[0] == 'Visa':
        return f'{from_data_split[0]} {from_data_split[1]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'

    return f'{from_data_split[0]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'

class Operation_information:
    def __init__(self, date, description, to_data, amount, currency_name):
        self.date = date
        self.description = description
        self.amount = amount
        self.currency_name = currency_name
        self.to_data = to_data
    def get_date_description(self):
        return f"{self.date} {self.description}"

    def get_data1(self, from_data):
        return f"{from_data} -> {self.to_data}"

    def get_data2(self):
        return self.to_data
    def get_operationAmount(self):
        return f"{self.amount} {self.currency_name}"



