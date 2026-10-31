import os
import requests
from dotenv import load_dotenv
import time

load_dotenv()

KEY=os.environ["NASA_API_KEY"]
url="https://api.nasa.gov/planetary/apod"
try:
  
  for attempt in range(3):
    response=requests.get(url,params={"api_key" :KEY},timeout=10)
    if response.status_code==200:
         break
    print(f"Attempt {attempt + 1} failed with status {response.status_code}")
    time.sleep(2 * (attempt + 1))
  data=response.json()
  print(type(data))
  print(data)
except requests.HTTPError as he:
  print(f"Http error is {he}")
except requests.RequestException as e:
  print(f"Conenction error as {e}")