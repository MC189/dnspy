import requests
from pprint import pprint
import json
uris = 'http://112.215.198.248'
client = requests.session()
params = { 'name': 'ns-indo.vpnjantit.com', 'type': 'NS', 'ct': 'application/dns-json' }
ae = client.get(uris, params = params, timeout = 1)
print(ae.status_code)