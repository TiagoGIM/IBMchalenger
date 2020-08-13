# IBMchalenger

Alguns exemplos de como usar as ferramentas da **IBM cloud** que aprendi durante o **_'Be hind the code 2020'_**. 

Os algoritimos foram feitos em ambiente linux (wsl). :bowtie:

###### Serviços abordados aqui:
- [x] Visual Recognition
- [ ] Watson Assistant
- [ ] Language Translator

## First Step

Crie uma conta na IBM cloud.

## Second Step

Instalar a biblioteca, eu usei o python3, se não for o seu caso basta retirar o '3' do comando.  

```
pip3 install --upgrade "ibm-watson>=4.5.0"
```

## Third Step
Inicie o serviço desejado para pegar as credênciais, URL e API KEY da aplicação.

## Fourth Step

* Retirar a linha que importa 'tokens'
```
from tokens import auths
```
* Subistituir os valores das variaveis _url_ e _api-key_ para a suas credênciais.

api_key = ~~auths['visualrecog']['api-key']~~
url = ~~auths['visualrecog']['url']~~

**obs.: Devem ser do tipo strings.**
## Links de referência

* [Visual recognition IBM](https://cloud.ibm.com/apidocs/visual-recognition/visual-recognition-v3?code=python)- IBM Cloud Documentation

Obs.: Até agora só testei o Visual recognition   =D

