import urllib3, requests, json
from watson_machine_learning_client import WatsonMachineLearningAPIClient
from tokens import ws #remova esta linha

"""
crie este objeto com suas credenciais
 ws ={
    "apikey"      :  "sua apeikey",
    "instance_id" : "seu instance id,
    "url"         : "https://us-south.ml.cloud.ibm.com",
}
"""

wml_credentials = ws

client = WatsonMachineLearningAPIClient( wml_credentials )

score_end_point = "https://us-south.ml.cloud.ibm.com/v3/wml_instances/0421bd9c-14a6-45fa-8fd7-177bde284374/deployments/c20ca4e9-d48c-4d82-ac98-e7cadbe1a6a8/online"

#payload de teste para validar treinamento

payload_scoring = {"fields": ["genero", "hobby", "viagem", "bebida"], "values": [['m','netflix','cidade','vinho']]}
#teste com payload e endpoint
resp = client.deployments.score(score_end_point,payload_scoring)

print(json.dumps(resp, indent=2))



  