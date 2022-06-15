

import pandas as pd
import os 

"""
title: Problems descriptions data generator
Created by: Natanael Domingos
version:    01
Description: 

    Gera arquivo com tipos de problemas. 

"""

# Diretórios de trabalho
WORK_DIR  = os.getcwd()
WORK_DATA = os.path.join(WORK_DIR, 'help_desk\data')

# Dicionário de Problemas 

problemas = [

    { 'id':3,  'tipo':'Instalação de Software'},
    { 'id':7,  'tipo':'Problemas de Rede/Internet'},
    { 'id':14, 'tipo':'Troca/Reset de Senhas'},
    { 'id':25, 'tipo':'Problemas de Hardware/Equipamentos'},
    { 'id':45, 'tipo':'Concessão de Acesso - Grupo AD'},
    { 'id':52, 'tipo':'Configurações de software'},
    { 'id':78, 'tipo':'Problemas de Infra e Reformas no ambiente'},

]



if __name__ == '__main__':

    # Gerando o arquivo CSV
    df = pd.DataFrame(problemas)
    df.to_csv( os.path.join(WORK_DATA, 'problemas.csv'), index=False,encoding='utf-8')

