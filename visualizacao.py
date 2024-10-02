import pandas as pd # type: ignore
import seaborn as sns # type: ignore
from sys import argv

def gerar_grafico(nome_grafico):
    # Extraindo as colunas hora e taxa
    df = pd.read_csv('./taxa-cdi.csv')

    # Criando o gráfico
    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
    _ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
    grafico.get_figure().savefig(f"{nome_grafico}.png")

    print(f"Gráfico '{nome_grafico}.png' gerado com sucesso.")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Uso correto: python visualizacao.py <nome-do-grafico>")
        exit(1)

    nome_grafico = argv[1]
    gerar_grafico(nome_grafico)
