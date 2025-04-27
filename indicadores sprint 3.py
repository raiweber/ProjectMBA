# Criar o gráfico com os dados fornecidos
import pandas as pd
import matplotlib.pyplot as plt

# Criar dataframe
data = {
    'Colaborador': [5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,6,6,6,6,6,1,1,1,1,2,2],
    'Atividade': ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Z','A1','B1'],
    'Esforco': [76,73,100,75,100,67,100,73,100,73,44,57,100,100,100,89,82,100,100,50,100,150,100,100,100,50],
    'Qualidade': [100,100,88,100,100,100,100,88,100,100,100,100,100,100,100,83,88,100,100,100,100,100,100,100,100,100]
}

df = pd.DataFrame(data)

# Configurar o gráfico
plt.figure(figsize=(15, 7))
x = range(len(df['Atividade']))
width = 0.35

# Criar barras com tons de marrom
plt.bar(x, df['Esforco'], width, label='Esforço (%)', color='#8B4513')  # Marrom escuro
plt.bar([i + width for i in x], df['Qualidade'], width, label='Qualidade (%)', color='#DEB887')  # Marrom claro

# Personalizar o gráfico
plt.xlabel('Atividade por Colaborador')
plt.ylabel('Percentual de Esforço e Qualidade')
plt.xticks([i + width/2 for i in x], [f'{a}\
(Col. {c})' for a, c in zip(df['Atividade'], df['Colaborador'])], rotation=45)
plt.legend()

plt.tight_layout()
plt.show()