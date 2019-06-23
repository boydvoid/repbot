import os
import json
def setup(name, password, directory):

    data = {}
    data['account'] = []
    data['account'].append({
        'username': name,
        'password': password,
        'directory': directory
    })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)