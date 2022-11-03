import requests
from lxml import html
endpoint = requests.get('http://localhost:8000').text
tree = html.fromstring(endpoint)

for tr in tree:
    print(tr.body)