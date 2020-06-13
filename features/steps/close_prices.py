from behave import *


@when('observing close price')
def step_impl(context):
    stocks = context.resp.json()
    context.close_prices=[stock['close'] for stock in stocks]
    print(context.close_prices)


@then('price must be greater than 0')
def step_impl(context):
    assert all(price >= 0 for price in context.close_prices)
