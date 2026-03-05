import os

# Limpa o terminal (cls para Windows, clear para Linux/Mac)
os.system('cls' if os.name == 'nt' else 'clear')

print("--- Resumo de Gastos por Categoria ---")


import pandas as pd
#1 carregar os dados
df = pd.read_csv('extrato.csv')

#2 garantir que a coluna 'valor' seja numerica
df['valor'] = pd.to_numeric(df['valor'])

#3 separra apenas os gastos (valores negativos)
gastos = df[df['valor'] < 0].copy()

#4 transformar os gastos em valores positivos para facilitar a leitura
gastos['valor'] = gastos['valor'].abs()

#5 agrupar por categoria e somar 
resumo = gastos.groupby('categoria')['valor'].sum().sort_values(ascending=False)

print('--- Resumo de Gastos por Categoria ---')
print('resumo')

#6 calcular o total de gastos
total_gasto = resumo.sum()
print(f'\nTotal gasto no mes: R${total_gasto:.2F}')

# Criando o texto que será salvo
texto_resumo = f"Total gasto no mes: R${resumo.sum():.2f}"

# Salvando em um arquivo chamado 'resultado.txt'
with open("resultado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("--- Resumo de Gastos por Categoria ---\n")
    arquivo.write(resumo.to_string()) # Salva a tabela do pandas
    arquivo.write(f"\n\n{texto_resumo}")

print("O arquivo 'resultado.txt' foi salvo com sucesso!")

#criacao de grafico para melhor visualizacao

import matplotlib.pyplot as plt

#criar o grafico de barras
resumo.plot(kind='bar', color="skyblue", edgecolor='black')

#adicionar rotulos e titulos
plt.title('Meus gastos por categoria')
plt.xlabel('Categoria')
plt.ylabel('valor (R$)')
plt.xticks(rotation=45) #inclina os nomes para nao amontoar

#salvar o grafico como uma imagem
plt.tight_layout()
plt.savefig('grafico_gastos.png')

#mostrar o grafico na tela
plt.show()