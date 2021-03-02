'''
Task 1
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc.
'''

import requests
import json

base_url = 'https://www.virtualsoccer.ru/player.php?num=4821250'

result = requests.get(base_url)
h = result.headers
c = result.content
s = result.status_code
data = json.dumps(str(h))
d_s = str(h)
print(d_s)
print(data)

f = open('robots.txt', 'w')
f.write(data)
f.close()


if __name__ == '__main__':
    pass

'''
---output---
{'Date': 'Tue, 02 Mar 2021 16:47:21 GMT', 'Expires': 'Tue, 02 Mar 2021 16:47:21 GMT', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Pragma': 'no-cache', 'Server': 'nginx', 'Last-Modified': 'Tue, 02 Mar 2021 16:47:21 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Set-Cookie': 'virtualsoccer_main=pvi110gh4278lno02bhnr6e8pn; expires=Wed, 02-Mar-2022 16:47:21 GMT; Max-Age=31536000; path=/; domain=.virtualsoccer.ru', 'Cache-Control': 'max-age=0, no-cache, no-store, must-revalidate'}
"{'Date': 'Tue, 02 Mar 2021 16:47:21 GMT', 'Expires': 'Tue, 02 Mar 2021 16:47:21 GMT', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Pragma': 'no-cache', 'Server': 'nginx', 'Last-Modified':
'Tue, 02 Mar 2021 16:47:21 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Set-Cookie': 'virtualsoccer_main=pvi110gh4278lno02bhnr6e8pn; expires=Wed, 02-Mar-2022 16:47:21 GMT; Max-Age=31536000; path=/; domain=.virtualsoccer.ru', 'Cache-Control': 'max-age=0, no-cache, no-store, must-revalidate'}"
'''
