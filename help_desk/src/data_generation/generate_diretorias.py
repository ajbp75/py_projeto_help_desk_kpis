

import pandas as pd
import os 

"""
title: Company's board descriptions data generator
Created by: Natanael Domingos
version:    01
Description: 

    Gera Diretórias dentro de uma empresa 

"""

# Diretórios de trabalho
WORK_DIR  = os.getcwd()
WORK_DATA = os.path.join(WORK_DIR, 'help_desk\data')

# Dicionário de Problemas 

diretorias = [

    { 'id':2,  'nome':'Marketing'},
    { 'id':4,  'nome':'Finanças'},
    { 'id':5,  'nome':'Operações'},
    { 'id':6,  'nome':'Tecnologia da Informação'},
    { 'id':7,  'nome':'Comercial'},
    { 'id':9,  'nome':'Recursos Humanos'},
    { 'id':11, 'nome':'Jurídico'},

]



if __name__ == '__main__':

    # Gerando o arquivo CSV
    df = pd.DataFrame(diretorias)
    df.to_csv( os.path.join(WORK_DATA, 'diretorias.csv'), index=False,encoding='utf-8')

