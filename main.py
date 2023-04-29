import requests

params = {"words": 10, "paragraphs": 1, "format": "json"}

response = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/", params=params,
 headers={
   "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
   "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
)

print (type(response.json()))
print(response.json())