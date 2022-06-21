import requests

url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

querystring = {"q":"peron","pageNumber":"1","pageSize":"1","autoCorrect":"true"}

headers = {
	"X-RapidAPI-Key": "6fb3a57ecemsh3faac6f662be92dp10e7b3jsn35ff00c16d10",
	"X-RapidAPI-Host": "contextualwebsearch-websearch-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)