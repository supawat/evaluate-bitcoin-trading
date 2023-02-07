# Project : Evaluate Bitcoin Trading
# Author : Supawat Kawmongkol
# City/Country : Bangkok Thailand
# Currency support USD and THB


import requests
import json

exchangerates_apikey = "qq9sWpAg0lQ2dSklTGmIZeX9Q3zZ3xZZ"

def exchangerates_data(apikey, symbols, base):

    # https://apilayer.com/
    # url = "https://api.apilayer.com/exchangerates_data/latest?symbols=THB&base=USD"

    url = "https://api.apilayer.com/exchangerates_data/latest?symbols="+symbols+"&base="+base

    payload = {}

    headers = {
        "apikey": apikey
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code

    result = response.text

    result_dict = json.loads(result)

    return result_dict["rates"]["THB"]

def get_bitcoin_price():

    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = r.json()

    rate_float = data["bpi"]["USD"]["rate_float"]

    return rate_float

def current_price():

    thb_rate = exchangerates_data(exchangerates_apikey, 'THB', 'USD')

    usd_rate = get_bitcoin_price()

    print("\n----- Current price of Bitcoin -----\n")

    print("Bitcoin USD Price : " + "{:,}".format(usd_rate))
    print("Bitcoin THB Price : " + "{:,}".format(thb_rate*usd_rate) + "\n")

    # print("Bitcoin USD Price : " + usd_currency.get_money_with_currency_format(usd_rate))
    # print("Bitcoin THB Price : " + thb_currency.get_money_with_currency_format(thb_rate*usd_rate) + "\n")


def inputBitcoinAmount(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            continue

        else:
            if userInput > 0:
                return userInput
            else:
                continue

def inputFeeExchangeRate(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            #print("Not an float! Try again.")
            continue

        else:
            if userInput >= 0 and userInput <= 100:
                return userInput
            else:
                continue

def inputCurrency(message):
    while True:
        try:
            userInput = input(message)
        except ValueError:
            #print("Not an float! Try again.")
            continue

        else:
            if userInput.lower() == 't' or userInput.lower() == 'u':
                return userInput
            else:
                continue

def inputFloatNumber(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            continue

        else:
            if userInput > 0:
                return userInput
            else:
                continue

def sell_bitcoin():
    print("\n----- Sell Bitcoin -----\n")
    bitcoin_amount = inputBitcoinAmount("Bitcoin amount : ")
    fee_exchange_rate = inputFeeExchangeRate("Fee exchange rate % : ")

    thb_rate = exchangerates_data(exchangerates_apikey, 'THB', 'USD')
    usd_amount = get_bitcoin_price() * bitcoin_amount
    fee_amount = ((usd_amount / 100) * fee_exchange_rate)
    usd_amount_deduct_fee = usd_amount - fee_amount


    print("\nYou will get USD amount : " + "{:,}".format(usd_amount_deduct_fee))
    print("USD fee : " + "{:,}".format(fee_amount))
    print("You will get THB amount : " + "{:,}".format(thb_rate*usd_amount_deduct_fee))
    print("THB fee : " + "{:,}".format(thb_rate*fee_amount)+ "\n")

def buy_bitcoin():

    print("\n----- Buy Bitcoin -----\n")

    currency = inputCurrency("Currency USD [U], THB [T] : ")

    if currency.lower() == 't':
        thb_amount = inputFloatNumber("THB Amount : ")
        fee_exchange_rate = inputFeeExchangeRate("Fee exchange rate % : ")

        thb_rate = exchangerates_data(exchangerates_apikey, 'THB', 'USD')

        usd_amount = thb_amount / thb_rate

        bitcoin_amount = usd_amount /get_bitcoin_price()

        fee_amount = ((bitcoin_amount / 100) * fee_exchange_rate)

        bitcoin_amount_deduct_fee = bitcoin_amount - fee_amount

        print("\nYou will get BTC amount : " + "{:,}".format(bitcoin_amount_deduct_fee))
        print("BTC fee : " + "{:,}".format(fee_amount) +"\n")

    else:
        usd_amount = inputFloatNumber("USD Amount : ")
        fee_exchange_rate = inputFeeExchangeRate("Fee exchange rate % : ")

        bitcoin_amount = usd_amount /get_bitcoin_price()

        fee_amount = ((bitcoin_amount / 100) * fee_exchange_rate)

        bitcoin_amount_deduct_fee = bitcoin_amount - fee_amount

        print("\nYou will get BTC amount : " + "{:,}".format(bitcoin_amount_deduct_fee))
        print("BTC fee : " + "{:,}".format(fee_amount) + "\n")

def main():

    print("\n----- Evaluate Bitcoin Trading -----\n")

    run_program = True

    while run_program:

        coin_operrate = input("Current price [C], SELL [S], BUY [B], Exit [Q] : ")

        if coin_operrate.lower() == 'c':
            current_price()

        elif coin_operrate.lower() == 's':
            sell_bitcoin()

        elif coin_operrate.lower() == 'b':
            buy_bitcoin()

        elif coin_operrate.lower() == 'q':
            run_program = False

if __name__ == "__main__":
    main()