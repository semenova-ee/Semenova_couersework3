import json
from src.functions import date_prettify, data_prettify, load_operations, Operation_information

operations = load_operations()

executed_operetions_counter = 0

while executed_operetions_counter < 5:
    raw = operations[executed_operetions_counter]
    date = date_prettify(raw["date"])
    description = raw["description"]
    amount = raw["operationAmount"]["amount"]
    currency_name = raw["operationAmount"]["currency"]["name"]
    to_data = data_prettify(raw["to"])

    if raw["state"] == "EXECUTED":
        executed = Operation_information(date, description, to_data, amount, currency_name)
        try:
            from_data = data_prettify(raw["from"])
            print(executed.get_date_description())
            print(executed.get_data1(from_data))
            print(executed.get_operationAmount())
            print()

        except KeyError:
            print(executed.get_date_description())
            print(executed.get_data2())
            print(executed.get_operationAmount())
            print()

    executed_operetions_counter += 1

