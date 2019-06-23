import os
import json
def setup(name, password):

    data = {}
    data['account'] = []
    data['account'].append({
        'username': name,
        'password': password,
    })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)