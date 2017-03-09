from twython import Twython
import csv

CONSUMER_KEY = 'wHA973TYHyNI5IlBNLnFW3UpP'
CONSUMER_SECRET = 'qamX0GIovNt6vUa32xsGQxQSlMcV6WwEjrJHQN7PqQajv2ppZg'
ACCESS_TOKEN = '839155364570476545-PWmQRvHI00R0xuUghImPdP3C0mlAiKZ'
ACCESS_TOKEN_SECRET = 'q9xhj7flAn0YoncQ4wbQ5XAaq937StOiAjwgj6pWXfebt'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='YOUR SEARCH TERM HERE', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['Lincoln Center', result['text'].encode('utf-8'), url]]
        a.writerows((text))
