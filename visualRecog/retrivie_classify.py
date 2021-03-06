import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#Este trecho deve ser retirado
from tokens import auths
#subistitua a api key e url pelas suas proprias credenciais.
api_key = auths['apikey']
url = auths['url']

authenticator = IAMAuthenticator(api_key)
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url(url)

# classifiers = visual_recognition.list_classifiers(verbose=True).get_result()

# print(json.dumps(classifiers, indent=2))

#print(classifiers['classifiers'][0]['classifier_id'])
#keys()
#for k, v in classifiers['classifiers'][0].items():
 #   print(k, v)
#for classify in classifiers['classifiers']:
#    if classify['status'] == 'failed':
#        print(' Classificador ', classify['classifier_id'], 'Não funciona')
#   else:
#       print(' Classificador ', classify['name'], 'Status :',classify['status'])
        #print(json.dumps(classify,indent=2))
done = True

while done:
    visual_recognition.set_service_url(url)
    classifiers = visual_recognition.list_classifiers(verbose=True).get_result()

    for classify in classifiers['classifiers']:
        if classify['classifier_id'] =="margarina_1067986790":
            if classify['status'] != "training":
                print(' Classificador :', classify['name'], ' | Status :',classify['status'])
                done = False
