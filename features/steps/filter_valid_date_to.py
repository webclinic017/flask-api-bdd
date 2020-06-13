from behave import *
import requests
from datetime import datetime


@given('{date_to} is the only query parameter')
def step_impl(context, date_to):
    url = f'http://127.0.0.1:5000/stocks?to={date_to}'
    context.resp = requests.get(url)


@when('observing results for {date_to}')
def step_impl(context, date_to):
    context.stocks = context.resp.json()
    context.stocks_from = min([stock['date'] for stock in context.stocks])
    context.stocks_to = max([stock['date'] for stock in context.stocks])


@then('no results after {date_to} display')
def step_impl(context, date_to):
    # diff is required to capture weekend case e.g. to=Sunday, but max available date=Friday
    diff = abs((datetime.strptime(date_to, "%Y-%m-%d") - datetime.strptime(context.stocks_to, "%Y-%m-%d")).days)
    assert diff <= 2


@then('only results from earliest available date display')
def step_impl(context):
    # get earliest date from unfiltered endpoint
    url = f'http://127.0.0.1:5000/stocks'
    resp = requests.get(url)
    unfiltered_stocks = resp.json()
    min_stocks_from = min([stock['date'] for stock in unfiltered_stocks])
    assert context.stocks_from == min_stocks_from
