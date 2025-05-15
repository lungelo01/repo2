#import the modules that we need
import json
import requests # Used to open a URL link in Python
# Open the URL
url = 'http://api.indeed.com/ads/apisearch?publisher=4407976915591140&q=java&l=austin&v=2&format=json'
response = requests.get(url)
# save the data in a json file
with open('data.json', 'w', encoding='utf-8') as outfile:
    outfile = json.dump(response.json(), outfile, sort_keys=True, indent=4)

with open('data.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)