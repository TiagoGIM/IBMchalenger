import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#Este trecho deve ser retirado
from tokens import auths
#subistitua a api key e url pelas suas proprias credenciais.
api_key = auths['visualrecog']['api-key']
url = auths['visualrecog']['url']

authenticator = IAMAuthenticator(api_key)
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url(url)

#testa se a porta é um dos objetos
classes = {}
with open('mesa.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file=images_file,
        threshold='0.6',
        owners=["me"]).get_result()        
    print(json.dumps(classes, indent=2))

