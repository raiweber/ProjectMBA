import pandas as pd
import matplotlib.pyplot as plt

# plot de dois gráficos em barra 

data_sprint2 = {
    'Colaborador': [1, 2, 4, 5, 6],
    'Esforço (%)': [0, 0, 35.7, 36.5, 27.8]
}

data_sprint3 = {
    'Colaborador': [1, 2, 4, 5, 6],
    'Esforço (%)': [16.7, 15.2, 50.9, 44.1, 44.1]
}

# DataFrames
df_sprint2 = pd.DataFrame(data_sprint2)
df_sprint3 = pd.DataFrame(data_sprint3)

# cria os dois plots lado a lado
plt.figure(figsize=(12, 6))

# Plot Sprint 2
plt.subplot(1, 2, 1)
plt.bar(df_sprint2['Colaborador'].astype(str), df_sprint2['Esforço (%)'], color='skyblue')
plt.title('Sprint 2 - % de esforço por colaborador (numérico)')
plt.xlabel('Colaborador')
plt.ylabel('% de Esforço')

# Plot Sprint 3
plt.subplot(1, 2, 2)
plt.bar(df_sprint3['Colaborador'].astype(str), df_sprint3['Esforço (%)'], color='salmon')
plt.title('Sprint 3 - % de esforço por colaborador (numérico)')
plt.xlabel('Colaborador')
plt.ylabel('% de Esforço')

plt.tight_layout()
plt.show()