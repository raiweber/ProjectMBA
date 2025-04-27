# Cria o gráfico com tons de marrom
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados originais
colaborador = [5,5,5,5,5,4,4,4,4,4,4,6,6,6,6,6,6,6,6,6]
atividade = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']
esforco = [133,138,100,100,114,200,100,100,125,200,100,200,100,200,100,200,100,100,100]
qualidade = [100,75,100,0,67,100,100,100,75,100,83,100,100,100,100,50,100,75,67]

colaborador = colaborador[:len(atividade)]

data = {'Colaborador': colaborador, 'Atividade': atividade, 'Esforco': esforco, 'Qualidade': qualidade}
df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))

x = range(len(df['Atividade']))
width = 0.35

# Usando tons de marrom
plt.bar(x, df['Esforco'], width, label='Esforço (%)', color='#8B4513')  # Marrom escuro
plt.bar([i + width for i in x], df['Qualidade'], width, label='Qualidade (%)', color='#DEB887')  # Marrom claro

plt.xlabel('Atividade por Colaborador')
plt.ylabel('Percentual de Esforço e Qualidade')
plt.xticks([i + width/2 for i in x], [f'{a}\
(Col. ' + str(c) + ')' for a, c in zip(df['Atividade'], df['Colaborador'])])
plt.legend()

plt.show()
