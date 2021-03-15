'''
Task 3 Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in chronological order in JSON and dump it to a file
'''

# [https://habr.com/ru/post/484446/]

import aiohttp
import asyncio
import requests
import json


session = aiohttp.ClientSession()
async def comm_ments(base_url):
    async with session.get(base_url) as response:
        result = await response.json()
        f = open('35b.txt', 'a')
        f.close()
        return result['results']


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(comm_ments('https://api.pushshift.io/reddit/comment/search/'))
    
