from operator import itemgetter
import requests
import json
from plotly.graph_objects import Bar
from plotly import offline

def safe_execute(default, exception, function, arg):
    try:
        return function(arg)
    except exception:
        return default

def return_response_dict(key):
    return response_dict[key]

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
readable_file = 'data/test.json'
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    with open(readable_file, 'a') as f:
        json.dump(response_dict, f, indent=4)

    # Build a dictionary for each article.
    submission_dict = {
        'id': response_dict['id'],
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': safe_execute(0, KeyError, return_response_dict, 'descendants'),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles, links, comms = [], [], [] # Used for the plot.
for submission_dict in submission_dicts:
    id = submission_dict['id']
    title = submission_dict['title']
    hyper = submission_dict['hn_link']
    link = f"<a href='{hyper}'>{id}</a>"
    comm = submission_dict['comments']
    print(f"\nTitle: {title}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
    titles.append(title)
    links.append(link)
    comms.append(comm)

# Let's plot the results.
data = [{
    'type': 'bar',
    'x': links,
    'y': comms,
    'hovertext': titles,
}]
my_layout = {

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='data/hn_plotted.html')