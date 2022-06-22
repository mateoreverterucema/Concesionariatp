import requests

url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"from":"EUR","to":"USD","q":"1.0"}

headers = {
	"X-RapidAPI-Key": "6fb3a57ecemsh3faac6f662be92dp10e7b3jsn35ff00c16d10",
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




""""
url = "https://google-image-search1.p.rapidapi.com/v2/"

querystring = {"q":"peron","hl":"en"}

headers = {
	"X-RapidAPI-Key": "6fb3a57ecemsh3faac6f662be92dp10e7b3jsn35ff00c16d10",
	"X-RapidAPI-Host": "google-image-search1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
"""