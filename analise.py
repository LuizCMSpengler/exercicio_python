from extracao import salvar_dados
from visualizacao import gerar_grafico
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Uso correto: python analise.py <nome-do-grafico>")
        exit(1)

    nome_grafico = argv[1]

    # Passo 1: Extrair os dados
    salvar_dados()

    # Passo 2: Gerar o gráfico
    gerar_grafico(nome_grafico)
