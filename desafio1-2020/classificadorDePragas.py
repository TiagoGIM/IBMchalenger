import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#Este trecho deve ser retirado
from tokens import auth
#subistitua a api key e url pelas suas proprias credenciais.
api_key = auth['apikey']
url = auth['url']

authenticator = IAMAuthenticator(api_key)
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url(url)
with open('./largataSoja.zip', 'rb') as lagarta, open(
        './percevejoMarrom.zip', 'rb') as percevejo_marrom, open(
            './percevejoPequeno.zip', 'rb') as percevejo_pequeno, open(
                './percevejoVerde.zip', 'rb') as percevejo_verde,
                    './falso.zip', 'rb') as false:
    model = visual_recognition.create_classifier(
        'objetos',
        positive_examples={'lagarta': lagarta, 'percevejo_marrom': percevejo_marrom, 'percevejo_pequeno': percevejo_pequeno},
        negative_examples=false).get_result()
print(json.dumps(model, indent=2))

"""
lagarta -> representando a lagarta de soja
percevejo_marrom -> representando o percevejo marrom
percevejo_pequeno -> repressantando o percevejo pequeno
percevejo_verde -> representnado o percevejo verde
"""