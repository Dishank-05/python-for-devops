import requests
import json


def get_cat_facts(url):
    try:
        resp = requests.get(url)
        response=resp.json()
        #print(type(response))
        fact_fetcher = response.get("fact") 
        print(fact_fetcher)
    except Exception as e:
        print("Unable to fetch cat facts:", e)


url = input("Enter API URL for facts you want:")

if url == '':
    print("No URL provided")
else:
    get_cat_facts(url)

