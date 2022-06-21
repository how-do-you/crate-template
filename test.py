import requests
import json
# https://api.github.com/repos/adaptive-simon/throwaway

r = requests.get("https://api.github.com/repos/adaptive-simon/throwaway")
data = json.loads(r.text)
print(data["description"])
#for n in data:
#    print(n)