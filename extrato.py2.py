import pandas as pd
import matplotlib.pyplot as plt

# 1. Configuração de Dados (O "Model" do seu sistema)
def carregar_dados(caminho_arquivo):
    # Lendo o CSV e garantindo que o Pandas entenda os números
    df = pd.read_csv(caminho_arquivo, decimal=',') 
    df['valor'] = pd.to_numeric(df['valor'])
    
    # Filtrando apenas gastos (negativos) e transformando em positivos
    gastos = df[df['valor'] < 0].copy()
    gastos['valor'] = gastos['valor'].abs()
    
    # Agrupando por categoria e somando
    return gastos.groupby('categoria')['valor'].sum().sort_values(ascending=False)

# 2. Geração Visual (A "View" do seu sistema)
def gerar_relatorio_visual(resumo):
    # Criando uma figura que comporta dois gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico 1: Barras (Valor exato por categoria)
    resumo.plot(kind='bar', ax=ax1, color='skyblue', edgecolor='black')
    ax1.set_title('Gastos por Categoria (R$)')
    ax1.set_xlabel('Categoria')
    ax1.set_ylabel('Valor Total')

    # Gráfico 2: Pizza (Percentual de cada gasto)
    resumo.plot(kind='pie', ax=ax2, autopct='%1.1f%%', startangle=140, shadow=True)
    ax2.set_title('Distribuição Percentual dos Gastos')
    ax2.set_ylabel('') # Limpa o rótulo lateral para ficar mais bonito

    # Salvando o resultado final como imagem
    plt.tight_layout()
    plt.savefig('relatorio_final.png')
    print("Relatório 'relatorio_final.png' salvo com sucesso!")
    
    # Mostrando a janela com os gráficos
    plt.show()

# --- Execução Principal ---
if __name__ == "__main__":
    try:
        dados_processados = carregar_dados('extrato.csv')
        gerar_relatorio_visual(dados_processados)
    except FileNotFoundError:
        print("Erro: O arquivo 'extrato.csv' não foi encontrado na pasta.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")