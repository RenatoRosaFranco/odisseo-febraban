import requests
import pandas
import json
import csv

# token = None
# authentication = {"username": "astrum", "password": "test123"}
# resp = requests.post('https://ciabhackathon.conductor.com.br:8443/auth',
#                      json=authentication,
#                      headers = {'Content-Type': 'application/json'})
#
# if resp.status_code != 200:
#     print('Erro')
# else:
#     token = resp.json()["token"]
#
# print("O valor de token é " + token)
#
# null = None
# dados = {
# 	"columns": ["idEventoCompra", "cartao", "dataCompra", "valorCompra", "numeroParcelas", "valorParcela", "idConta", "idEstabelecimento", "codigoMoedaDestino", "dataEmissao", "dataValidade", "estadoCivil", "numeroDependentes", "empresa", "tempoTrabalhoAnos", "profissao", "salario", "sexo", "cpf", "dataNascimento", "limiteCredito", "cep", "uf", "tempoResidenciaAnos"],
# 	"filters": {
# 	  "numeroCartao": null,
# 	  "dataInicio": null,
# 	  "dataFim": null,
# 	  "valorMinimo": null,
# 	  "valorMaximo": null,
# 	  "salarioMinimo": 1900,
# 	  "salarioMaximo": 8000,
# 	  "idadeMinima": null,
# 	  "idadeMaxima": null,
# 	  "limiteMinimo": null,
# 	  "limiteMaximo": null,
# 	  "nClusters": 4
# 	}
# }
#
# def traine_model(body, token):
#
#     body_json = body
#     resp = requests.post('https://ciabhackathon.conductor.com.br:8443/comportamento/kmeans/train',
#                          json=body_json,
#                          headers={'Content-Type': 'application/json',
#                                   'Authorization': token})
#
#     if resp.status_code != 200:
#         print("Deu errado")
#     else:
#         print("Funcionou")
#
# traine_model(dados, token)

from pandas import DataFrame

def get_by_salary(min, max):
    uri = "https://ciabhackathon.conductor.com.br:8443/transacoes/data/intervalo/2018-05-01/2018-07-01"
    resp = requests.get(uri,
                         headers = {'Content-Type': 'application/json',
                                    'Authorization': 'Token a754f3d7bffaf8abc2570d5c354f8f4015e5487e'})

    if resp.status_code != 200:
        print("Deu errado")
    else:
        result = resp.json()['data']
        csv = DataFrame(result)
        export_csv = csv.to_csv(r'file.csv')

get_by_salary('1900', '2700')