# from app import create_app
# import urllib.request, json
# from .models import Quotes
# from flask_script import Manager,Server


# base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

# def get_quotes():

#     with urllib.request.urlopen(base_url) as url:
#         get_quotes_data = url.read()
#         get_quotes_response = json.loads(get_quotes_data)
#         if get_quotes_response:
#             quote_results_list = get_quotes_response
#             quote_results = process_results(quote_results_list)

#     return quote_results

# def process_results(quote_list):

#         quote_results = []
#         for quote_item in quote_list:

#             author = quote_item.get('author')
#             quote = quote_item.get('quote')

#             quote_object = Quotes(author, quote)
#             quote_results.append(quote_object)

#         return quote_results
