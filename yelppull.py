from DataCollector import data_collector
import json
import requests
import pandas as pd

with open('keys.json') as file:
    keys = json.load(file)
YELP_KEY = keys.get('yelp')

initial_data = pd.read_csv('clean_data_initial.csv')

yelp_list = []
for index in initial_data.index:
    d = data_collector(initial_data, index, YELP_KEY)
    yelp_list.append(d)

with open('apipull', 'w') as fout:
    json.dump(yelp_list, fout)
