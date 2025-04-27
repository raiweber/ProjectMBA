# Importar libs
import pandas as pd
import matplotlib.pyplot as plt

# Dataframe
data = {
    'Colaborador': ['1', '2', '3', '4', '5', '6'],
    'Total_horas': [26, 4, 4, 112, 40, 48],
    'Projeto_SU': [36.00, 0.00, 8.00, 40.00, 16.00, 0.00],
    'Projeto_S17': [0.00, 2.56, 0.00, 97.44, 0.00, 0.00],
    'Projeto_LA': [0.00, 4.35, 0.00, 0.00, 0.00, 95.65],
    'Projeto_D': [13.33, 0.00, 0.00, 26.67, 53.33, 6.67]
}

df = pd.DataFrame(data)

# Criar um gráfico de barras empilhadas para mostrar o esforço percentual de cada projeto por colaborador
fig, ax = plt.subplots(figsize=(10, 6))

# Posições no eixo x
ind = range(len(df))

# Plotar cada projeto como uma pilha
p1 = ax.bar(ind, df['Projeto_SU'], label='Projeto SU')
p2 = ax.bar(ind, df['Projeto_S17'], bottom=df['Projeto_SU'], label='Projeto S17')
p3 = ax.bar(ind, df['Projeto_LA'], bottom=df['Projeto_SU'] + df['Projeto_S17'], label='Projeto LA')
p4 = ax.bar(ind, df['Projeto_D'], bottom=df['Projeto_SU'] + df['Projeto_S17'] + df['Projeto_LA'], label='Projeto D')

# Configurar labels e título
ax.set_xticks(ind)
ax.set_xticklabels(df['Colaborador'])
ax.set_ylabel('Percentual de esforço (%)')
ax.set_xlabel('Colaborador')
ax.set_title('Distribuição de esforço por Projeto para cada Colaborador')

# Remover grades e cor de fundo
ax.grid(False)
fig.patch.set_facecolor('white')  # Fundo da figura
ax.set_facecolor('white')          # Fundo do gráfico

# Adicionar legenda
ax.legend()

# Melhorar layout
plt.tight_layout()

# Mostrar gráfico
plt.show()
