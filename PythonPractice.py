import requests

url = 'http://api.open-notify.org/astros.json'
r = requests.get(url)
data = r.json()
names = [record['name'] for record in data]

print(data)
print(data['number'])
print(data['people'])
print(data['people'][0])
print(data['people'][0]['name'])
print(names)


Update from Surface
