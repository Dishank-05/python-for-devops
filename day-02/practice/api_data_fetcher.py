import requests
import json

resp = requests.get("https://meowfacts.herokuapp.com/")
#print(resp.json()

facts_data = resp.json().get("data")[0]
print (facts_data)
with open ("cat_facts.json", "w") as f:
    json.dump(facts_data, f)