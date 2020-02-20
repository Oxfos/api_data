import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process and explore results.
response_dict = r.json()
for k, v in response_dict.items():
    print(f"{k}: {v}")

# Store results in a readable way.
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)