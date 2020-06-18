import requests
import csv

URL='http://127.0.0.1:5000/stocks'


def before_scenario(context, scenario):

    if 'api' in context.tags:
        context.resp = requests.get(URL)

    if scenario.name == 'Endpoint is built as per initial from/to dates':
        with open('./var/initial_dates.csv', 'r') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for row in csv_reader:
                context.date_from = row[0]
                context.date_to = row[1]
        print(f"""
    =======================================================
    Test dates must be between {context.date_from} and {context.date_to}.
    =======================================================""")

def before_feature(context, feature):
    if feature.name == 'Filter on dates':
        context.resp = requests.get(URL)
        stocks = context.resp.json()
        date_from = min([stock['date'] for stock in stocks])
        date_to = max([stock['date'] for stock in stocks])
        print(f"""
    =======================================================
    Test dates must be between {date_from} and {date_to}.
    =======================================================""")








