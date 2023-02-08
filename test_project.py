from project import exchangerates_data , get_bitcoin_price, inputFeeExchangeRate
import pytest
import sys
import io

apikey = "qq9sWpAg0lQ2dSklTGmIZeX9Q3zZ3xZZ"
symbols = 'THB'
base = 'USD'

def main():

    test_exchangerates_data()
    test_get_bitcoin_price()
    test_inputFeeExchangeRate()


def test_exchangerates_data():
    value = exchangerates_data(apikey, symbols, base)
    assert isinstance(value, float)
    assert value > 0 

def test_get_bitcoin_price():
    value = get_bitcoin_price()
    assert isinstance(value, float)
    assert value > 0

def test_inputFeeExchangeRate(capsys):

    input_str = "0.25"
    sys.stdin = io.StringIO(input_str)

    value = inputFeeExchangeRate("Fee exchange rate % : ")

    captured = capsys.readouterr()
    assert "Fee exchange rate % : " in captured.out
    assert isinstance(value, float)


if __name__ == "__main__":
    main()