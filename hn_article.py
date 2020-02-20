import requests

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
for k, v in response_dict.items():
    print(f"{k}: {v}")
