# IBMchalenger

Alguns exemplos de como usar as ferramentas da IBM cloud que aprendi durante o 'Be hind the code 2020'. :bowtie:

Os algoritimos foram feitos em ambiente linux (wsl)

# Serviços abordados aqui:
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
´´´´
~~from tokens import auths~~
´´´´
* Subistituir os valores das variaveis url e api-key com suas credênciais.
´´´
api_key = ~~auths['visualrecog']['api-key']~~
url = ~~auths['visualrecog']['url']~~
´´´´
## Links de referência

* [Visual recognition IBM](https://cloud.ibm.com/apidocs/visual-recognition/visual-recognition-v3?code=python)- IBM Cloud Documentation

Obs.: Até agora só testei o Visual recognition   =D

