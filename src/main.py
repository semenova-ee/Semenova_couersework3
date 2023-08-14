import json
from src.functions import date_prettify, data_prettify

with open('operations.json', encoding='utf8') as file:
    operations = json.load(file)

print(operations)
# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.

executed_operetions_counter = 0

while executed_operetions_counter < 5:
    raw = operations[executed_operetions_counter]
    if raw["state"] == "EXECUTED":
        try:
            print(f'{date_prettify(raw["date"])} {raw["description"]}')
            print(f'{data_prettify(raw["from"])} -> {data_prettify(raw["to"])}')
            print(f'{raw["operationAmount"]["amount"]} {raw["operationAmount"]["currency"]["name"]}')
            print()

        except KeyError:
            print(data_prettify(raw["to"]))
            print(f'{raw["operationAmount"]["amount"]} {raw["operationAmount"]["currency"]["name"]}')
            print()

        executed_operetions_counter += 1


