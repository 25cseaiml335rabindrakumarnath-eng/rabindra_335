import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=song&limit=100&term=" + sys.argv[1])
a = response.json()

for results in a["results"]:
    print(results["trackName"])

