import requests, json

def get_movie_info(title, year):
	url = "http://www.omdbapi.com/?t=" + title+ "&y=" + year + "=&plot=short&r=json"
	response = requests.get(url)
	data = json.loads(response.text)
	return data


