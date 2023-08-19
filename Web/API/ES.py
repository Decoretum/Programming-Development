import requests

urlOne = 'http://localhost:8000/api/citizens/view?name=Justin&spec=softWare DeveLopment'

response = requests.get(urlOne)

rawResponse = response.json()[0]

print(rawResponse.get("uniqueID"))