
# web "client" fetches web page, given a URL
## when asked, it checks its cache for the web page

# first request: fetches from the interwebz
# second request: returns from cache

# Why?
## Faster, increased speed
## Decrease load on web server
## Security
## Cuts down calls to APIs


# Hash table usage to make a web client cache?
## URL could be the key
## web page data could be the value


# Problems with our naive implementation?
## 'every successful complex system will be found to have evolved from a simple system'
## what if the actual page changes? Our data will be old - stale
## No size limitation - end up storing the internet

# How to solve these problems?
## How to solve stale data in the cache?
### timeout: after a week, go and fetch again, even if it's already in cache

## Problem of storing too much - size?
### Monetize??
### LRU cache - set a max number of items
### timestamp every item and sweep through periodically

import urllib.request

url = 'https://www.google.com'

cache = {}

page = None
# check if we have previously gotten this url
if url in cache:
    page = cache[url]

    # compare timestamp to check if it's timed out

# if not, go fetch it
else:
    print('getting from server')

    # fetch the data
    resp = urllib.request.urlopen(url)
    data = resp.read()

    # put in the cache
    cache[url] = data

    page = cache[url]

print(page)