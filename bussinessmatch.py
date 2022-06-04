
import requests
import pandas as pd
import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))

url = 'https://api.yelp.com/v3/businesses/search'
key = os.getenv("API_KEY")
headers = {
    'Authorization' : 'bearer %s' % key
}
parameters = {
    'term' : 'BBQ',
    'limit' : 50,
    'radius' : 10000,
    'location' : 'Duluth'
}
response = requests.get(url = url, headers=headers, params=parameters)

query = response.json()['businesses']

results = {'Name': [],'Price': [],'Rating': [],'Reviews': [],}
for q in query:
    results['Name'].append(q['name'])
    if "price" in q.keys():
        results['Price'].append(len(q['price']))
    else:
        results['Price'].append(0)      
    results['Rating'].append(q['rating'])
    results['Reviews'].append(q['review_count'])
    

pd.DataFrame(results)