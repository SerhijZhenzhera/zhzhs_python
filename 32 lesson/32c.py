'''
Task 3.Requests using multiprocessing
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in chronological order in JSON and dump it to a file.
For this task use Threads for making requests to reddit API.
'''

# [https://creativedata.stream/multi-threading-api-requests-in-python/]

import requests
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed

url_list = ['url1', 'url2']

def download_file(url, file_name):
    try:
        html = requests.get(url, stream=True)
        open(f'{file_name}.json', 'wb').write(html.content)
        return html.status_code
    except requests.exceptions.RequestException as e:
       return e

def runner():
    threads= []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for url in url_list:
            file_name = uuid.uuid1()
            threads.append(executor.submit(download_file, url, file_name))
           
        for task in as_completed(threads):
            print(task.result()) 
      



if __name__ == '__main__':

    runner()

    
'''
---output---

'''
