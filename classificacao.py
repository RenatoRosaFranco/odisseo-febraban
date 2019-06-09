"""
    1. Se ele é gordinho
    2. Se ele tem perninha curta
    3. Se ele faz auau
"""
porco1    = [1, 1, 0]
porco2    = [1, 1, 0]
porco3    = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
marcacoes = [1, 1, 1, -1, -1, -1]

# [é gordinho?, tem perninha curta?, faz auau?
# -1=(cachorro), (1)=porco
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
marcacaoes_teste = [misterioso1, misterioso2, misterioso3]

def prediz_tipo(collection):
    for data in collection:
        if (data == 1):
            print('Porco')
        else:
            print('Cachorro')


from sklearn.naive_bayes import MultinomialNB
import numpy as np

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
resultado = modelo.predict(marcacaoes_teste)
prediz_tipo(resultado)
diferencas = resultado - marcacaoes_teste

acertos = [d for d in diferencas if any(d == 0)]
print(acertos)
total_de_acertos = len(acertos)
print(total_de_acertos)