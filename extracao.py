import os
import time
import json
from random import random
from datetime import datetime
import requests # type: ignore

URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'


def extrair_taxa_cdi():
    # Captando a taxa CDI do site do BCB
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
    except requests.HTTPError:
        print("Dado não encontrado, continuando.")
        return None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        return float(json.loads(response.text)[-1]['valor'])


def salvar_dados():
    dado = extrair_taxa_cdi()

    if dado is None:
        print("Não foi possível obter a taxa CDI.")
        return

    for _ in range(10):
        data_e_hora = datetime.now()
        data = datetime.strftime(data_e_hora, '%Y/%m/%d')
        hora = datetime.strftime(data_e_hora, '%H:%M:%S')
        cdi = dado + (random() - 0.5)

        # Verificando se o arquivo "taxa-cdi.csv" existe
        if not os.path.exists('./taxa-cdi.csv'):
            with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
                fp.write('data,hora,taxa\n')

        # Salvando dados no arquivo "taxa-cdi.csv"
        with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
            fp.write(f'{data},{hora},{cdi}\n')

        time.sleep(1)

    print("Dados extraídos com sucesso.")


if __name__ == "__main__":
    salvar_dados()