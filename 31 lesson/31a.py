'''
Task 1
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc.
'''

import requests
import json

base_url = 'https://www.virtualsoccer.ru'

result = requests.get(base_url+'/robots.txt')
c = result.content
# data = c.json()
data = json.dumps(str(c))
f = open('robots.txt', 'w')
f.write(data)
f.close()


if __name__ == '__main__':
    pass

'''
---output---

'''
