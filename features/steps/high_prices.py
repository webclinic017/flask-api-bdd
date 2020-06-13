from behave import *
import requests


# @given('API is up and running again')
# def step_impl(context):
#     url = 'http://127.0.0.1:5000'
#     context.resp = requests.get(url)


@when('observing high price')
def step_impl(context):
    stocks = context.resp.json()
    context.prices={stock['high']:stock['close'] for stock in stocks}
    print(context.prices)


@then('price must be greater than or equal to close price')
def step_impl(context):
    assert all(high_price >= close_price for high_price, close_price in context.prices.items())
