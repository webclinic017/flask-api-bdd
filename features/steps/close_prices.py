from behave import *
import requests


# @given('API is up and running again')
# def step_impl(context):
#     url = 'http://127.0.0.1:5000'
#     context.resp = requests.get(url)


@when('observing close price')
def step_impl(context):
    stocks = context.resp.json()
    context.close_prices=[stock['close'] for stock in stocks]
    print(context.close_prices)


@then('price must be greater than 0')
def step_impl(context):
    assert all(price >= 0 for price in context.close_prices)
