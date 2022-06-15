

import pandas as pd
import os 

"""
title: Departments descriptions data generator
Created by: Natanael Domingos
version:    01
Description: 

    Gera arquivo com registros de Departamentos. 

"""

# Diretórios de trabalho
WORK_DIR  = os.getcwd()
WORK_DATA = os.path.join(WORK_DIR, 'help_desk\data')

# Dicionário de Problemas 

departamentos = [

    { 'id':41, 'nome':'Data Science',       'id_diretoria':6, },
    { 'id':45, 'nome':'Web Development',    'id_diretoria':6, },
    { 'id':47, 'nome':'Sales',              'id_diretoria':7, },
    { 'id':48, 'nome':'Tech Recruit',       'id_diretoria':9, },
    { 'id':49, 'nome':'Exportação',         'id_diretoria':5, },
    { 'id':55, 'nome':'Logística',          'id_diretoria':5, },
    { 'id':56, 'nome':'Regulação e Normas', 'id_diretoria':11,}

]



if __name__ == '__main__':

    # Gerando o arquivo CSV
    df = pd.DataFrame(departamentos)
    df.to_csv( os.path.join(WORK_DATA, 'departamentos.csv'), index=False,encoding='utf-8')

