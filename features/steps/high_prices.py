from behave import *


@when('observing high price')
def step_impl(context):
    stocks = context.resp.json()
    context.prices={stock['high']:stock['close'] for stock in stocks}
    print(context.prices)


@then('price must be greater than or equal to close price')
def step_impl(context):
    assert all(high_price >= close_price for high_price, close_price in context.prices.items())
