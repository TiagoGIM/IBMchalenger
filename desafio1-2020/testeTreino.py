import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from sys import argv # caso queria escolher o nome da img, digite no terminal >>  python3 testeImage.py nome.jpg

from tokens import auths # IMPORTANTE: Este trecho deve ser retirado

#subistitua a api key e url pelas suas proprias credenciais.
api_key = auths['visualrecog']['api-key']
url = auths['visualrecog']['url']
imgteste = imgteste = argv[1:]  #nome do arquivo de imagem que quer testar


authenticator = IAMAuthenticator(api_key)
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url(url)

#testa se a porta é um dos objetos
classes = {}

for img in imgteste:
    with open(img, 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file=images_file,
            threshold='0.6',
            owners=["me"]).get_result()        
        for img in classes['images']:
            for classs  in img['classifiers']:
                if 'classes'in classs:
                    for c in classs['classes']: #é uma lista
                        print(c['class'],c['score'])


                
                
            