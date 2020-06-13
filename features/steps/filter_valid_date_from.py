from behave import *
import requests
from datetime import datetime

@given('only {date_from} provided as query parameter')
def step_impl(context, date_from):
    url = f'http://127.0.0.1:5000/stocks?from={date_from}'
    context.resp = requests.get(url)


@when('observing results filtered based on {date_from}')
def step_impl(context, date_from):
    context.stocks = context.resp.json()
    context.stocks_from = min([stock['date'] for stock in context.stocks])
    context.stocks_to = max([stock['date'] for stock in context.stocks])


@then('no results before {date_from} display')
def step_impl(context, date_from):
    # diff is required to capture weekend case e.g. from=Saturday, but min available date=Monday
    diff = abs((datetime.strptime(context.stocks_from, "%Y-%m-%d") - datetime.strptime(date_from, "%Y-%m-%d")).days)
    assert diff <= 2


@then('only results to maximum available date display')
def step_impl(context):
    # get latest date from unfiltered endpoint
    url = f'http://127.0.0.1:5000/stocks'
    resp = requests.get(url)
    unfiltered_stocks = resp.json()
    max_stocks_to = max([stock['date'] for stock in unfiltered_stocks])
    assert context.stocks_to == max_stocks_to
