import json
#reading the credentials from secure plase
f = open('/home/joseba/credentials/keys.json',)
data = json.load(f)
print(data["keys"]["telegram_key"])

