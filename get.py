import requests

# GET method
r = requests.get('http://104.236.109.213/items')
print(r.text)