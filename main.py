import requests
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
    'term' : 'coffee',
    'limit' : '50',
    'radius' : 40000,
    'location' : 'Atlanta'
}
response = requests.get(url = url, headers=headers, params=parameters)

business_data = response.json()

print(business_data.keys())

for biz in business_data['businesses']:
    print(biz['name'])