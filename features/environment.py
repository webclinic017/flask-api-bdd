import requests


URL='http://127.0.0.1:5000/stocks'

def before_scenario(context, scenario):
    if 'api' in context.tags:
        context.resp = requests.get(URL)

def before_feature(context, feature):
    if feature.name == 'Filter on dates':
        context.resp = requests.get(URL)
        stocks = context.resp.json()
        from_date = min([stock['date'] for stock in stocks])
        to_date = max([stock['date'] for stock in stocks])
        print(f"""
    =======================================================
    Test dates must be between {from_date} and {to_date}.
    =======================================================""")




