from behave import *
import requests



@given('{date_from} and {date_to} provided as query parameters')
def step_impl(context, date_from, date_to):
    url = f'http://127.0.0.1:5000/stocks?from={date_from}&to={date_to}'
    context.resp = requests.get(url)


@when('observing filtered data')
def step_impl(context):
    context.stocks = context.resp.json()
    context.stocks_from = min([stock['date'] for stock in  context.stocks])
    context.stocks_to = max([stock['date'] for stock in  context.stocks])


@then('results display')
def step_impl(context):
    assert len(context.stocks) > 0


@then('there are no records before {date_from}')
def step_impl(context, date_from):
    assert context.stocks_from == date_from

@then('there are no records after {date_to}')
def step_impl(context, date_to):
    assert context.stocks_to == date_to
