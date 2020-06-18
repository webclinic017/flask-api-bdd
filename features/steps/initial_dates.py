from behave import *
import requests
from datetime import datetime, timedelta
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
    dt_date_from = datetime.strptime(context.date_from, "%Y-%m-%d")  # convert to datetime
    if dt_date_from.isoweekday() in range(1, 6):  # check if day in in weekday 1 (Monday) to 5 (Friday)
        assert context.stocks_from == context.date_from
    else:  # if day is 6 (Saturday) or 7 (Sunday)
        nearest_date = dt_date_from + timedelta(days=8 - dt_date_from.isoweekday())  # get nearest expected date
        str_nearest_date = nearest_date.strftime('%Y-%m-%d')  # convert back to string
        assert context.stocks_from == str_nearest_date  # compare against nearest date


@then('last available date is the initial To date')
def step_impl(context):
    dt_date_to = datetime.strptime(context.date_to, "%Y-%m-%d")  # convert to datetime
    if dt_date_to.isoweekday() in range(1, 6):  # check if day in in weekday 1 (Monday) to 5 (Friday)
        print(dt_date_to)
        assert context.stocks_to == context.date_to
    else:  # if day is 6 (Saturday) or 7 (Sunday)
        nearest_date = dt_date_to - timedelta(days=dt_date_to.isoweekday() - 5)  # get nearest expected date
        str_nearest_date = nearest_date.strftime('%Y-%m-%d')  # convert back to string
        print(str_nearest_date)
        assert context.stocks_to == str_nearest_date  # compare against nearest date
