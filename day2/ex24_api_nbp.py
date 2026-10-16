import requests

url = 'https://api.nbp.pl/api/exchangerates/tables/A/'

response = requests.get(url)
print(response)
# <Response [200]>

print(response.text)

print(25 * "*")
dane = response.json() # zamiana na słownik
print(dane[0])
print(25 * "*")
print(dane[0]['rates'][1]['currency'])
print(dane[0]['rates'][1]['mid'])
