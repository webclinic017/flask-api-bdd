from behave import *
import requests


@given('API is up and running')
def step_impl(context):
    url='http://127.0.0.1:5000/stocks'
    context.resp = requests.get(url)


@when('observing a stock')
def step_impl(context):
    context.stock=context.resp.json()[0]
    #print(context.stock)


@then('{key} should show on position {order}')
def step_impl(context, key, order):
    #print('index', list(context.stock.keys()).index(key))
    try:
        assert list(context.stock.keys()).index(key) == int(order)
    except AssertionError:
        print(f'Expected index {order}, but got {list(context.stock.keys()).index(key)}.')
        raise



