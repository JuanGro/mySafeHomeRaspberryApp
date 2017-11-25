import requests

# GET method
'''
r = requests.get('http://104.236.109.213/items')
print(r.text)
'''

# Object to send
payload = {
        'type': 'Fire',
        'date': '2017-11-17 16:01:29',
        'location': 'Living room'
}

files = {
        'image': open('images/image3.jpg', 'rb')
}

# POST method
r = requests.post('http://104.236.109.213/item', data = payload, files = files)
print(r)