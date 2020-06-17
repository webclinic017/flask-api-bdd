from behave import *
import requests
from datetime import datetime
import csv


@given('API is created')
def step_impl(context):
    url = f'http://127.0.0.1:5000/stocks'
    context.resp = requests.get(url)


@when('viewing the endpoint')
def step_impl(context):
    context.stocks = context.resp.json()
    context.stocks_from = min([stock['date'] for stock in context.stocks])
    context.stocks_to = max([stock['date'] for stock in context.stocks])


@then('first available date is the initial From date')
def step_impl(context):
    with open('./var/initial_dates.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            context.date_from = row[0]
    print(context.date_from)
    assert context.stocks_from == context.date_from


@then('last available date is the initial To date')
def step_impl(context):
    with open('./var/initial_dates.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            context.date_to = row[1]
    print(context.date_to)
    assert context.stocks_to == context.date_to
