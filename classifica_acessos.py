from sklearn.naive_bayes import MultinomialNB
from dados import carregar_acessos
import math

X, Y = carregar_acessos()
modelo = MultinomialNB()
modelo.fit(X, Y)

# Testes
# 1 vai comprar, 0 não vai comprar
# [home, planos, contato]
resultado = modelo.predict(X)
diferencas = resultado - Y

treino_dados = X[:90]
treino_marcacoes = X[:90]

teste_dados = X[-9:]
teste_marcacoes = X[-9:]

acertos = [d for d in diferencas if d == 0]
total_de_acertos   = len(acertos)
total_de_elementos = len(X)
total_de_acertos   = (100.0 * total_de_acertos) / total_de_elementos

# Resultados
print(math.ceil(total_de_acertos))
print(total_de_elementos)