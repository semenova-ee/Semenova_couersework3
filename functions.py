from main import operations
date = '2019-08-26T10:50:58.294041'
def date_prettify(date: str) -> str:
    date_new = date[0:10].split('-')
    date_new = ".".join(ch for ch in reversed(date_new))
    return date_new

print(date_prettify(date))

a="Счет 75106830613657916952"
b= "MasterCard 7158300734726758"
c="Visa Gold 5999414228426353"
def data_prettify(from_data: str) -> str:
    from_data_split = from_data.split(' ')
    num = from_data_split[-1]
    if from_data_split[0] == 'Счет':
        return f'{from_data_split[0]} **{num[-4:]}'

    if from_data_split[0] == 'Visa':
        return f'{from_data_split[0]} {from_data_split[1]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'

    return f'{from_data_split[0]} {num[0:4]} {num[4:6]}** **** {num[-4:]}'


print(from_data(a))
print(from_data(b))
print(from_data(c))
