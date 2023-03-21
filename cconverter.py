import requests

if __name__ == "__main__":
    currency_code = input().lower()
    rates = requests.get(
        f"http://www.floatrates.com/daily/{currency_code}.json").json()
    cache = dict()
    if currency_code != 'usd':
        cache['usd'] = float(rates["usd"]['rate'])

    if currency_code != 'eur':
        cache['eur'] = float(rates["eur"]['rate'])

    while True:
        exchange_currency = input().lower()
        if len(exchange_currency) == 0:
            break
        amount = float(input())
        print('Checking the cache...')
        received_rate = float(rates[exchange_currency]['rate'])
        if exchange_currency in cache:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            cache[exchange_currency] = received_rate
        result = round(amount * received_rate, 2)
        print(
            f'You received {round(amount * cache[exchange_currency], 2)} {exchange_currency.upper()}.')
