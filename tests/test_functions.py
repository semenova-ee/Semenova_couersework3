from src.functions import date_prettify, data_prettify, OperationInformation, sort_data


def test_date_prettify():
    """Проверяет преобразование даты в формат ДД.ММ.ГГГГ"""
    assert date_prettify("2023-08-13T12:34:56") == "13.08.2023"
    assert date_prettify("2022-05-01T18:45:30") == "01.05.2022"
    assert date_prettify("2018-03-09T02:11:01.339352") == "09.03.2018"


def test_data_prettify():
    """Проверяет преобразование счета в формат **ХХХХ и номера карты в формат ХХХХ ХХ** **** ХХХХ"""
    assert data_prettify("Счет 75106830613657916952") == "Счет **6952"
    assert data_prettify("Visa Platinum 7000123456786361") == "Visa Platinum 7000 12** **** 6361"
    assert data_prettify("MasterCard 5555123456787890") == "MasterCard 5555 12** **** 7890"

raw = {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
       'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
       'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}
t_1 = OperationInformation(raw)


def test_operation_information():
    """Проверяет вывод информации об операции клиента"""
    assert t_1.get_date_description() == "07.12.2019 Перевод организации"
    assert t_1.get_data1('Visa Classic 2842 87** **** 9012') == "Visa Classic 2842 87** **** 9012 -> Счет **3655"
    assert t_1.get_operation_amount() == "48150.39 USD"
    assert t_1.get_data2() == "Счет **3655"


t_2 = [
    {
        "state": "EXECUTED",
        "date": "2018-01-21T01:10:28.317704"
    },
    {
        "state": "EXECUTED",
        "date": "2019-09-29T14:25:28.588059"
    }
]


def test_sort_data():
    """Проверяет сортировку списка по статусу и дате"""
    assert sort_data(t_2) == [{'state': 'EXECUTED', 'date': '2019-09-29T14:25:28.588059'},
                              {'state': 'EXECUTED', 'date': '2018-01-21T01:10:28.317704'}]
