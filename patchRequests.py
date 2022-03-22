import requests
import json

# URL INICIAL   
URL = "https://www.leagueoflegends.com/page-data/en-us/news/tags/patch-notes/page-data.json"

r = requests.get(URL)
data = []
datafiltrada = []
# RETORNA UM JSON COM TODA A INFORMACAO DO SITE  E JOGA NUMA VARIAVEL COMO UM JSON OBJECT
v = json.loads(r.content)

# ACHA A PARTE DO JSON COM A INFORMACAO DOS LINKS
for item in v['result']['data']['articles']['nodes']:
    # PRA CADA LINK ENCONTRADO NO JSON ELE VAI FAZER UM REQUEST PRA INFORMACAO ESPECIFICA SOBRE O PATCH
    URL = "https://www.leagueoflegends.com/page-data/en-us/" + item['url']['url'] + "page-data.json"
    patch = requests.get(URL)
    # JOGA O CONTEUDO NUM CAMPO DATA PARA PEGAR TUDO
    data.append(json.loads(patch.content))
    # OU PODE JOGAR O JSON EM UMA VARIAVEL E TRABALHAR AS INFORMACOES PRA CRIAR UM JSON FILTRADO
    datapatch = json.loads(patch.content)
    # CRIACAO DE UM JSON (NAO CONSEGUI FAZER PARA SEPARAR A PARTE DOS PATCH NOTES)
    c = {
         "Titulo": datapatch['result']['data']['all']['nodes'][0]['title'],
         "Descrição": datapatch['result']['data']['all']['nodes'][0]['description']
    }
    datafiltrada.append(c)
    print(c)
