

from   faker import Faker
import pandas as pd
import random 
from   datetime import datetime, timedelta
import os

"""

title: Gerador de chamados
Created by: Natanael Domingos
version:    01
Description: 

    Gera conjunto de dados sobre solicitações/chamados no Help Desk. 

"""

# Diretórios de trabalho
WORK_DIR  = os.getcwd()
DATA_DIR  = os.path.join(WORK_DIR, 'help_desk\data')

# Variáveis 
Faker.seed(42)   # configurando uma seed para replicar resultado randomicos futuramente
fake = Faker()   # criando objeto 

# Gera Lista de Chamados
def gera_chamados( qtd_chamados ):

    """

    Gera uma lista de chamados aleatórios, contendo dados como:
        . dt_abertura     - quando o chamado foi aberto 
        . dt_aprovacao    - quando o chamado foi aprovado pelo gestor imediato
        . dt_resolucao    - quando o chamado foi resolvido e entregue para validação do usuário.
        . dt_fechamento   - encerramento do chamado após validação, se o usuário não validar em 3 dias o chamado será fechado automaticamente 
        . cod_problema    - código do tipo do problema
        . id_solicitante
        . id_departamento
        . id_diretoria
        
    in  - qtd_chamados - quantidade de chamados a serem gerados
    out - lista_chamados - lista com chamados gerados
    
    """
    
    # Listas de referências
    lista_funcionarios  = pd.read_csv(os.path.join(DATA_DIR,'funcionarios.csv'))['id'].unique() 
    lista_problemas     = pd.read_csv(os.path.join(DATA_DIR,'problemas.csv'))['id'].unique()
    lista_diretorias    = pd.read_csv(os.path.join(DATA_DIR,'diretorias.csv'))['id'].unique() 
    lista_departamentos = pd.read_csv(os.path.join(DATA_DIR,'departamentos.csv'))['id'].unique()
    lista_de_chamados   = []
   
    # Variávies locais
    start_datetime = datetime.strptime('2020-01-01 00:00:01', '%Y-%m-%d %H:%M:%S')  # data inicial dos chamados abertos
    end_datetime   = 'now'


    for n in range(1,qtd_chamados + 1):
        
        random_days = random.randint(1,90)  # quantidade randomica de dias entre 1  e 90
        random_hours = random.randint(1,48)
        
        dt_abertura   = fake.date_time_between(   start_date = start_datetime, end_date   = end_datetime)
        dt_aprovacao  = dt_abertura +  timedelta( hours=random_hours)
        dt_resolucao  = dt_aprovacao + timedelta( days=random_days)
        dt_fechamento = dt_resolucao + timedelta( hours=random_hours)

        chamado = {

            'dt_abertura':     dt_abertura,
            'dt_aprovacao':    dt_aprovacao,
            'dt_resolucao':    dt_resolucao,
            'dt_fechamento':   dt_fechamento,
            'cod_problema':    random.choice(lista_problemas),
            'id_solicitante':  random.choice(lista_funcionarios),
            'id_departamento': random.choice(lista_departamentos),
            'id_diretoria':    random.choice(lista_diretorias)

        }


        lista_de_chamados.append(chamado)

    return lista_de_chamados


if __name__ == '__main__':
    chamados = gera_chamados( 5000 ) # gera n registros randomicos de chamados
    # Grava como CSV
    pd.DataFrame(chamados).to_csv( os.path.join(DATA_DIR, 'chamados.csv'), index=False,encoding='utf-8')
 
                                          

