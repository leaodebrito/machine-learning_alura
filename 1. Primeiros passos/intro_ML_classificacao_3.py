import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#from sklearn.svm import LinearSVC
#from sklearn.metrics import accuracy_score

#importação CSV
uri = '1. Primeiros passos/projects.csv'
dados = pd.read_csv(uri)


#mudança do títulos das colunas
mapa = {
    'expected_hours': 'horas_esperadas',
    'price': 'preco',
    'unfinished': 'nao_finalizado'
}
dados = dados.rename(columns=mapa)

#ajuste de valores para nova coluna 'finalizado'
troca = {
    1:0,
    0:1
}
dados['finalizado'] = dados.nao_finalizado.map(troca)


#plotagem de gráficos usando seaborn
#plotar usando mathplotlib

print(sns.scatterplot(x='horas_esperadas', y='preco', hue='finalizado', data=dados))
sns.relplot(x = "horas_esperadas", y = "preco",hue = "finalizado", col = "finalizado", data=dados)