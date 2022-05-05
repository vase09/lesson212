import pytest

from main import double


def test_double():
    assert double(2) == 4


def test_ticket_price_0():
    assert ticket_price(0) == "Бесплатно", "Ошибка для 0 лет"


def test_ticket_price_1():
    assert ticket_price(1) == "Бесплатно", "Ошибка для 1 лет"


def test_ticket_price_7():
    assert ticket_price(7) == "100 рублей", "Ошибка для 7 лет"


def test_ticket_price_18():
    assert ticket_price(18) == "200 рублей", "Ошибка для 18 лет"


def test_ticket_price_25():
    assert ticket_price(25) == "300 рублей", "Ошибка для 25 лет"


def test_ticket_price_60():
    assert ticket_price(60) == "Бесплатно", "Ошибка для 60 лет"


def test_ticket_price_minus_1():
    assert ticket_price(-1) == "Ошибка", "Ошибка для -1 лет"