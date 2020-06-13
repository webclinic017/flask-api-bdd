from behave import *
import requests


@given('{date_from} and {date_to} provided as invalid query parameters')
def step_impl(context, date_from, date_to):
    url = f'http://127.0.0.1:5000/stocks?from={date_from}&to={date_to}'
    context.resp = requests.get(url)


@when('observing results')
def step_impl(context):
    context.stocks = context.resp.json()


@then('no results display')
def step_impl(context):
    assert len(context.stocks) == 0

