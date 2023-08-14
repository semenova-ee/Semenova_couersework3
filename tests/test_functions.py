from src.functions import date_prettify, data_prettify

def test_date_prettify():
    assert date_prettify("2023-08-13T12:34:56") == "13.08.2023"
    assert date_prettify("2022-05-01T18:45:30") == "01.05.2022"
    assert date_prettify("2018-03-09T02:11:01.339352") == "09.03.2018"

def test_data_prettify():
    assert data_prettify("Счет 75106830613657916952") == "Счет **6952"
    assert data_prettify("Visa Platinum 7000123456786361") == "Visa Platinum 7000 12** **** 6361"
    assert data_prettify("MasterCard 5555123456787890") == "MasterCard 5555 12** **** 7890"