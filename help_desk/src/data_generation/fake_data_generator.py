from faker import Faker
from datetime import datetime
import random

"""
Created by: Natanael Domingos
version:    01
Description: 

    O objetivo deste script é gerar uma base de dados de chamados abertos entre 2020 até o momento. 

"""

fake = Faker()

start_datetime = datetime.strptime('2020-01-01 00:00:01', '%Y-%m-%d %H:%M:%S')
end_datetime   = 'now'

values = []

for n in range(100):

    
    # Data da abertura dos chamados, valores aleatórios a partir de 2020
    dt_abertura = fake.date_time_between(

        start_date = start_datetime,
        end_date   = end_datetime

    )


    # Data de Aprovação  - Após aberto, armazena a data da aprovação pelo gestor.
    # Data da Resolução  - Data da resolução do pedido, entrando em fase de validação do solicitante até finalização do chamado
    # Data do Fechamento - Após validada a resolução o chamado é fechado. Se o usuário não validar em até 3 dias úteis o chamado é finalizado automaticamente
    # Código do problema informado
    cod_problem = random.randint(3,24)
    # Descrição do problema informado
    # Nome do Solicitante
    # Área do Solicitante
    # Diretoria do Solicitante
    # Gestor Imediato do Solicitante

    ticket = {'dt_abertura':dt_abertura, 'cod_problem':cod_problem}


    values.append(ticket)


for tickets in values:
    print('* Data Abertura: {}, Código do Problema: {}'.format(tickets['dt_abertura'],tickets['cod_problem']))