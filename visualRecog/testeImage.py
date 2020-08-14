import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from sys import argv # caso queria escolher o nome da img, digite no terminal >>  python3 testeImage.py nome.jpg

from tokens import auths # IMPORTANTE: Este trecho deve ser retirado

#subistitua a api key e url pelas suas proprias credenciais.
api_key = auths['visualrecog']['api-key']
url = auths['visualrecog']['url']
imgteste = ""  #nome do arquivo de imagem que quer testar

if imgteste == "":    #pega nome da imagem direto do terminal
    imgteste = argv[1:][0]     

authenticator = IAMAuthenticator(api_key)
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url(url)

#testa se a porta é um dos objetos
classes = {}
with open(imgteste, 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file=images_file,
        threshold='0.6',
        owners=["me"]).get_result()        
    #print(json.dumps(classes, indent=2))
    for img in classes['images']:
        #print('primeiro loop  :', img)   #lista com classificadores
        for classs  in img['classifiers']:
            if 'classes'in classs:
                for c in classs['classes']: #é uma lista
                    print(c['class'],c['score'])
            #for k, y in classs.items():
                #print("%s é %s"% (k,y))
                
                
            