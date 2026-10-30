import requests

######one way of try catch block
#try:
#  response=requests.get("https://api.github.com/users/this-user-does-not-exist-12345")
#   if response.status_code==200:
       
#     print(response.status_code)
#     data=response.json()
#     print(type(data))
#     print(data)
#     print(data["login"])
#     print(data["public_repos"])
#   else: 
#        print(f"Error: {response.status_code}")

#except requests.RequestException as e:
#    print(f"Network problem: {e}")
########second way of try catch block
#url="https://api.github.com/users/octocat"
#try:
#     response=requests.get(url,timeout=10)
#     response.raise_for_status()
#     data=response.json()
#     print(data["login"])
#except requests.HTTPError as http_err:
#    print(f"HTTP error occurred: {http_err}")  
#except requests.RequestException as req_err:
#    print(f"Networkerror occurred: {req_err}")   

import requests

try:
    response = requests.get("https://this-site-does-not-exist-12345.com", timeout=10)
    #response = requests.get("http://localhost:9999", timeout=10)
    #response = requests.get("https://api.github.com/users/octocat", timeout=10)
    print(response.status_code)
#except requests.RequestException as e:
 #   print(f"Network problem: {e}")
except requests.RequestException as e:
    print(type(e).__name__, "-", e)

     
