import requests
headers = {'X-Api-Key': '0058a1e7b9a648259e3e52e129f5902c'}
url = 'https://randommer.io/api/Card'
r = requests.get(url, headers=headers).json()
print(r)
