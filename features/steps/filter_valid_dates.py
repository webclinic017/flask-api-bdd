from behave import *
import requests
from datetime import datetime, timedelta


@given('{date_from} and {date_to} provided as query parameters')
def step_impl(context, date_from, date_to):
    url = f'http://127.0.0.1:5000/stocks?from={date_from}&to={date_to}'
    context.resp = requests.get(url)


@when('observing filtered data')
def step_impl(context):
    context.stocks = context.resp.json()
    context.stocks_from = min([stock['date'] for stock in context.stocks])
    context.stocks_to = max([stock['date'] for stock in context.stocks])
    context.weekday_from = datetime.strptime(context.stocks_from, "%Y-%m-%d").isoweekday() # get "from" as weekday
    context.weekday_to = datetime.strptime(context.stocks_to, "%Y-%m-%d").isoweekday() # get "to" as weekday
    # print(context.weekday_from, context.weekday_to)
    # print(context.stocks_from)


@then('results display')
def step_impl(context):
    assert len(context.stocks) > 0


@then('there are no records before {date_from}')
def step_impl(context, date_from):
    dt_date_from=datetime.strptime(date_from,"%Y-%m-%d")   # convert to datetime
    if dt_date_from.isoweekday() in range(1,6):       # check if day in in weekday 1 (Monday) to 5 (Friday)
        assert context.stocks_from == date_from
    else:          # if day is 6 (Saturday) or 7 (Sunday)
        nearest_date=dt_date_from + timedelta(days=8-dt_date_from.isoweekday())  # get nearest expected date
        str_nearest_date = nearest_date.strftime('%Y-%m-%d')    # convert back to string
        assert context.stocks_from == str_nearest_date     # compare against nearest date

@then('there are no records after {date_to}')
def step_impl(context, date_to):
    dt_date_to=datetime.strptime(date_to,"%Y-%m-%d")   # convert to datetime
    if dt_date_to.isoweekday() in range(1,6):       # check if day in in weekday 1 (Monday) to 5 (Friday)
        assert context.stocks_from == date_to
    else:          # if day is 6 (Saturday) or 7 (Sunday)
        nearest_date=dt_date_to - timedelta(days=dt_date_to.isoweekday() - 5)  # get nearest expected date
        str_nearest_date = nearest_date.strftime('%Y-%m-%d')    # convert back to string
        print(str_nearest_date)
        print(dt_date_to.isoweekday())
        assert context.stocks_to == str_nearest_date     # compare against nearest date