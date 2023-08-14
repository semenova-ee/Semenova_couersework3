from src.functions import data_prettify, load_operations, OperationInformation, sort_data

operations = load_operations()
client_transactions = sort_data(operations)

operetions_counter = 0

while operetions_counter < 5:
    raw = client_transactions[operetions_counter]
    executed = OperationInformation(raw)

    try:
        from_data = data_prettify(raw["from"])
        print(executed.get_date_description())
        print(executed.get_data1(from_data))
        print(executed.get_operation_amount())
        print()

    except KeyError:
        print(executed.get_date_description())
        print(executed.get_data2())
        print(executed.get_operation_amount())
        print()

    operetions_counter += 1
