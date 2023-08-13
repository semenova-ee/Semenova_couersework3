import json

with open('operations.json', encoding='utf8') as file:
    operations = json.load(file)

print(operations)
# Пример вывода для одной операции:
# 14.10.2018 Перевод организации
# Visa Platinum 7000 79** **** 6361 -> Счет **9638
# 82771.72 руб.

description = []
from_data = []
to_data = []
operation_amount = []

print(operations[0]['date'])