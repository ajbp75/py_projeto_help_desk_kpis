
from   faker import Faker
import pandas as pd
import random
import os 

Faker.seed(42)
fake = Faker()

"""
title: Problems descriptions data generator
Created by: Natanael Domingos
version:    01
Description: 

    Gera arquivo com dados dos funcionários. 

"""

# Diretórios de trabalho
WORK_DIR  = os.getcwd()
WORK_DATA = os.path.join(WORK_DIR, 'help_desk\data')


# Gera Lista de Cargos com pesos para determinar a quantidade de funcionários em cada cargo.
def cargos_ponderados(qtd_funcionarios):

    """

        Gera uma lista de cargos randomicas considerando pesos para cada um.
        Quanto maior o peso maior a quantidade de funcionários com o cargo. 

        in  -> qtd_funcionarios - quantidade de cargos a serem retornados
        out -> random_cargos    - lista com labels do cargos

    """

    # Cargos existentes na empresa
    lista_de_cargos = ['Analista','Diretor','Gerente','Recrutador','Advogado','Cientista de Dados','Engenheiro de Dados','Motorista','Vendedor']

    # Pesos para cada um dos cargos. O peso representa a quantidade de funcionários por cargo, quanto maior o peso maior a quantidade
    pesos_por_cargo = [30,1,3,5,5,10,20,35,40]

    random_cargos = random.choices(lista_de_cargos, k=qtd_funcionarios, weights=pesos_por_cargo)

    return random_cargos
    


# Cria uma base de Funcionários
def gera_funcionarios( qtd_funcionarios ):

    """

    in  -> qtd_funcionarios      = Recebe como parâmetro a quantidade de funcionários a serem criados.
    out -> lista_de_funcionarios = Gera uma lista de funcionários contendo as informações:      
            . nome
            . id
            . id_departamento
            . cargo

    """

    lista_de_departamentos = [41,45,47,48,49,55,56]          # lista com ids de todos os departamentos existentes na empresa.
    lista_de_funcionarios  = []                              # vai armazenar um dicionários com dados de cada funcionário criado.
    lista_de_cargos  = cargos_ponderados(qtd_funcionarios)   # labels com o cargo de cada novo funcionário.

    # Cria Funcionário com informações randomicas
    for n in range(1, qtd_funcionarios):        

        funcionario = {

            'id'  : random.randint(100,2000),
            'nome': fake.name(),
            'id_departamento': random.choice(lista_de_departamentos),
            'cargo': lista_de_cargos[n]

        }

        lista_de_funcionarios.append(funcionario)

    return lista_de_funcionarios



if __name__ == '__main__':

    lista_de_funcionarios = gera_funcionarios(500)
    
    # Gerando o arquivo CSV
    df = pd.DataFrame(lista_de_funcionarios)
    df.to_csv( os.path.join(WORK_DATA, 'funcionarios.csv'), index=False,encoding='utf-8')

