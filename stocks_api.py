from flask import Flask, json, jsonify, request
from dateutil import parser
import requests


REQ_ALL = 'https://eodhistoricaldata.com/api/eod/AAPL.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&fmt=json'

class StockMarket():
    def __init__(self, name):
        self.name = name

    def _fetch_data(self, req):
        """Fetches json data on given request"""
        resp = requests.get(req)
        return resp.json()

    def fetch_all(self):
        """Fetch all available data"""
        print("Fetching all data...")
        return self._fetch_data(REQ_ALL)

    def fetch_filtered(self, date_from, date_to):
        """Fetch data based on dates"""
        self.date_from = parser.parse(date_from).strftime("%Y-%m-%d")
        self.date_to = parser.parse(date_to).strftime("%Y-%m-%d")
        req_date = f'https://eodhistoricaldata.com/api/eod/AAPL.US?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&period=d.&from={self.date_from}&to={self.date_to}&fmt=json'
        print("Fetching filtered data...")
        return self._fetch_data(req_date)

    def __repr__(self):
        return f'{self.name}'


def all_or_filtered():
    """This relates to Decide whether to fetch all stocks or filter on dates."""
    apple = StockMarket('AAPLUS')
    choice = input('Extract all available data from https://eodhistoricaldata.com for AAPL.US? Y/N: ')

    if choice.upper() == 'Y':
        output = apple.fetch_all()
        print("Done.")
    else:
        print('Choose Filter Dates')
        input_from = input('Date from: ')
        input_to = input('Date to: ')
        date_from = parser.parse(input_from).strftime("%Y-%m-%d")
        date_to = parser.parse(input_to).strftime("%Y-%m-%d")
        output = apple.fetch_filtered(date_from, date_to)
        print("Done.")
    return output


api = Flask(__name__)
api.config['JSON_SORT_KEYS'] = False  # keep order of keys in stocks json


@api.route('/')
def home():
    """Basic root page of API"""
    endpoint_link = request.base_url + "stocks"
    return f"""<h1>Stock Data API</h1>
    <ul>
         <li>
            <h3>Stock data
                <a class="toclick" href={endpoint_link} /> here </a>
            </h3>
        </li>
        <li>
            <h3>Query parameter usage:</h3>
            <p>Optional 'from' and 'to' query parameters are available</p>
            <p>Examples: '/stocks?from=2019-04-10&to=2019-04-14' or '/stocks?from=2019-04-10' or '/stocks?to=2019-03-25'</p> 
        </li>
    </ul>
    """


@api.route('/stocks')
def endpoint_filter():
    """Allow optional usage of date from - to filters, either individually or as a pair."""

    if 'from' in request.args and 'to' in request.args:
        date_from = request.args['from']
        date_to = request.args['to']
    elif ('from' in request.args) and not ('to' in request.args):
        date_from = request.args['from']
        date_to = max(stock['date'] for stock in stocks)
    elif not ('from' in request.args) and ('to' in request.args):
        date_from = min(stock['date'] for stock in stocks)
        date_to = request.args['to']
    else:
        return jsonify(stocks)

    results = [stock for stock in stocks if date_from <= stock['date'] <= date_to]
    return jsonify(results)


if __name__ == '__main__':
    stocks = all_or_filtered()
    api.run()
