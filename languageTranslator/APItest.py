import requests
from tokens import auth
# NOTE : este script ainda não funciona  =D
"""
Ainda não descobri como fazer o post com autenticação
"""

apikey = auth['apikey']
print(auth['apikey'])
url = auth['url']

dados ={"text": ["Hello, world.", "How are you?"], "model_id":"en-es"}

custom_header = {"content-type": "application/json","username":"apikey", "password":apikey}
print(custom_header)
r = requests.post(url+"/v3/translate?version=2018-05-01", headers = custom_header, json= dados, )

print(r.text)
