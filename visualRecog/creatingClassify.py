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
with open('./chair.zip', 'rb') as chair, open(
        './glass.zip', 'rb') as glass, open(
            './water_bottle.zip', 'rb') as water_bottle, open(
                './door.zip', 'rb') as door:
    model = visual_recognition.create_classifier(
        'objetos',
        positive_examples={'chair': chair, 'glass': glass, 'water_bottle': water_bottle},
        negative_examples=door).get_result()
print(json.dumps(model, indent=2))