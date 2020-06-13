from behave import *


@when('observing low price')
def step_impl(context):
    stocks = context.resp.json()
    context.prices={stock['low']:stock['close'] for stock in stocks}
    print(context.prices)


@then('price must be less than or equal to close price')
def step_impl(context):
    assert all(low_price <= close_price for low_price, close_price in context.prices.items())
