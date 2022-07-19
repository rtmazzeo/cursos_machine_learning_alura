# -*- coding: utf-8 -*-
"""machine_learning_01

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KFx2kY8GLG_4Cf0-qMOuOUgR2lItxo9I

**Aula 01**

A ideia desse primeiro projeto é usar o machine learning para diferenciar dois animais com características diferentes: um porco e um cachorro.
"""

#Será usada classificação binária: 0 = Cachorro e 1 = Porco (Classificação)
#Usaremos 3 caractéristica: (Features)

#  0 = Pelo Curto e 1 = Pelo Longo
#  0 = Perna Longa e 1 = Perna Curta
#  0 = não faz 'Au Au' e 1 = faz 'Au au'

porco1 = [0,1,0]
porco2 = [0,1,1]
porco3 = [1,1,0]

cachorro1 = [0,1,1]
cachorro2 = [1,0,1]
cachorro3 = [1,1,1]

treino_x = [porco1,porco2,porco3,cachorro1,cachorro2, cachorro3]
treino_y = [ 1,1,1,0,0,0] #labels

#importando a biblioteca que será usada
from sklearn.svm import LinearSVC

#estanciando o LinearSVC
model = LinearSVC()

#treinando o modelo
model.fit(treino_x,treino_y)

#verificando a previsão do modelo ( 0 = cachorro ,  1 = porco)

animal_misterioso = [1,1,1]
model.predict([animal_misterioso])

#verificando a previsão do modelo ( 0 = cachorro ,  1 = porco)

misterio1 = [1,1,1]
misterio2 = [1,1,0]
misterio3 = [0,1,1]

teste_x = [misterio1,misterio2,misterio3]
teste_y = [0,1,1] #o resultado real do misterio1, misterio2 e misterio3 é [0,1,1]

previsoes = model.predict(teste_x)

#comparação dos resultados previstos com o resultado real
previsoes == teste_y

#Taxa de Acerto

corretos = (previsoes == teste_y).sum() #numero de corretos (verdadeiro)
total = len(teste_y)
taxa_de_acerto = corretos/total
print('Taxa de Acertos: %.2f'%(taxa_de_acerto*100), '%')

"""Calculando a taxa de acerto usando o sklearn - accuracy_score"""

from sklearn.metrics import accuracy_score

taxa_de_acerto = accuracy_score(teste_y,previsoes)
print('Taxa de Acertos: %.2f'%(taxa_de_acerto*100), '%')

"""## **Projeto 2 - Classificação**
--- 
Utilizando uma nova fonte de dados

"""

import pandas as pd
uri = 'https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv'
dados = pd.read_csv(uri)

mapa = { 
    'home':'principal',
    'how_it_works':'como_funciona',
    'contact': 'contato',
    'bought': 'comprado'}

dados = dados.rename(columns = mapa)

x = dados[['principal','como_funciona','contato']]
y = dados['comprado']

"""Separando o treino do teste"""

dados.shape

#iremos separar 75% dos dados para treinar o algoritimo
treino_x = x[:75]
treino_y = y[:75]
teste_x = x[75:]
teste_y = y[75:]

print('Treinaremos com %d elementos e testaremos com %d elementos' %(len(treino_x),len(teste_x)))

modelo = LinearSVC()
modelo.fit(treino_x,treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y,previsoes) * 100

print('Taxa de Acertos: %.2f'%(acuracia), '%')

"""**Usando a biblioteca para separar treino e teste**"""

from sklearn.model_selection import train_test_split

SEED = 20

treino_x, teste_x,treino_y, teste_y = train_test_split(x,y,
                                                       random_state = SEED, 
                                                       stratify = y, # para que a proporção dos que compraram e não compraram sejam semelhantes (comparaveis)
                                                       test_size =0.25)

modelo = LinearSVC()
modelo.fit(treino_x,treino_y)
previsoes = modelo.predict(teste_x)
acuracia = accuracy_score(teste_y,previsoes) * 100

print('Taxa de Acertos: %.2f'%(acuracia), '%')

"""## Testando duas Dimensões
---
"""

import pandas as pd
uri = 'https://gist.githubusercontent.com/guilhermesilveira/1b7d5475863c15f484ac495bd70975cf/raw/16aff7a0aee67e7c100a2a48b676a2d2d142f646/projects.csv'
dados = pd.read_csv(uri)

mapa = { 
    'unfinished':'nao_finalizado',
    'expected_hours':'horas_esperadas',
    'price': 'preco'}

dados = dados.rename(columns = mapa)

dados.head()

troca = {0:1,1:0}

dados['finalizado'] = dados.nao_finalizado.map(troca)

dados.tail(5)

import seaborn as sns

sns.scatterplot(x='horas_esperadas',y='preco', data=dados)

import seaborn as sns

sns.scatterplot(x='horas_esperadas',y='preco', hue='finalizado', data=dados)

sns.relplot(x='horas_esperadas',y='preco', hue = 'finalizado', col='finalizado', data=dados)

x = dados[['horas_esperadas', 'preco']]
y = dados['finalizado']

SEED = 1

treino_x, teste_x,treino_y, teste_y = train_test_split(x,y,
                                                       random_state = SEED, 
                                                       stratify = y, # para que a proporção dos que compraram e não compraram sejam semelhantes (comparaveis)
                                                       test_size =0.25)

modelo = LinearSVC()
modelo.fit(treino_x,treino_y)
previsoes = modelo.predict(teste_x)
acuracia = accuracy_score(teste_y,previsoes) * 100

print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))
print('Taxa de Acertos: %.2f'%(acuracia), '%')

import numpy as np
previsoes_de_base = np.ones(540)
acuracia = accuracy_score(teste_y,previsoes_de_base)*100
print('A acurácia do algoritmo de baseline: %.2f'%(acuracia), '%')

"""**Curva de Decisão**
---

"""

sns.scatterplot(x='horas_esperadas',y='preco', hue = teste_y, data=teste_x)

x_min = teste_x.horas_esperadas.min()
x_max = teste_x.horas_esperadas.max()
y_min = teste_x.preco.min()
y_max = teste_x.preco.max()
print(x_min,x_max,y_min,y_max)

pixels = 100
eixo_x = np.arange(x_min,x_max, (x_max - x_min) / pixels)
eixo_y = np.arange(y_min,y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(eixo_x, eixo_y)
pontos = np.c_[xx.ravel(), yy.ravel()]
pontos

z = modelo.predict(pontos)
z = z.reshape(xx.shape)
z

import matplotlib.pyplot as plt

plt.contourf(xx,yy,z,alpha=0.3)
plt.scatter(teste_x.horas_esperadas, teste_x.preco, c=teste_y,s=1)

"""Observamos que o algoritmo que estamos utilizando só é capaz de aprender uma linha reta, que não serve para classificação. Precisamos de algum modelo estimador que seja capaz de aprender um padrão mais inteligente.

## Estimadores não lineares e support vector machine
"""

from sklearn.svm import SVC

SEED = 5
np.random.seed(SEED)
treino_x, teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)
print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))

modelo = SVC()
modelo.fit(treino_x,treino_y)
previsoes = modelo.predict(teste_x)
acuracia = accuracy_score(teste_y,previsoes) * 100

print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))
print('Taxa de Acertos: %.2f'%(acuracia), '%')

x_min = teste_x.horas_esperadas.min()
x_max = teste_x.horas_esperadas.max()
y_min = teste_x.preco.min()
y_max = teste_x.preco.max()

pixels = 100
eixo_x = np.arange(x_min,x_max, (x_max - x_min) / pixels)
eixo_y = np.arange(y_min,y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(eixo_x, eixo_y)
pontos = np.c_[xx.ravel(), yy.ravel()]

z = modelo.predict(pontos)
z = z.reshape(xx.shape)

plt.contourf(xx,yy,z,alpha=0.3)
plt.scatter(teste_x.horas_esperadas, teste_x.preco, c=teste_y,s=1)

#Padronizar os dados em uma faixa de valor específico
from sklearn.preprocessing import StandardScaler

SEED = 5
np.random.seed(SEED)
raw_treino_x, raw_teste_x, treino_y, teste_y = train_test_split(x, y, test_size = 0.25,
                                                         stratify = y)

scaler = StandardScaler()
scaler.fit(raw_treino_x)
treino_x = scaler.transform(raw_treino_x)
teste_x = scaler.transform(raw_teste_x)

modelo = SVC()
modelo.fit(treino_x,treino_y)
previsoes = modelo.predict(teste_x)
acuracia = accuracy_score(teste_y,previsoes) * 100

print("Treinaremos com %d elementos e testaremos com %d elementos" % (len(treino_x), len(teste_x)))
print('Taxa de Acertos: %.2f'%(acuracia), '%')

data_x = teste_x[:,0]
data_y = teste_x[:,1]

x_min = data_x.min()
x_max = data_x.max()
y_min = data_y.min()
y_max = data_y.max()

pixels = 100
eixo_x = np.arange(x_min,x_max, (x_max - x_min) / pixels)
eixo_y = np.arange(y_min,y_max, (y_max - y_min) / pixels)

xx, yy = np.meshgrid(eixo_x, eixo_y)
pontos = np.c_[xx.ravel(), yy.ravel()]

z = modelo.predict(pontos)
z = z.reshape(xx.shape)

plt.contourf(xx,yy,z,alpha=0.3)
plt.scatter(data_x, data_y, c=teste_y,s=1)

