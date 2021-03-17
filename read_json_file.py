
import json
#Read the json file
with open("data.JSON","r") as f:
	data=json.load(f)

print(data['records'][0])
print(data['records'][0]['name'])