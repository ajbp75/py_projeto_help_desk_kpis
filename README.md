# Monitoramento de SLAS - Chamados Help Desk

Partindo do zero, desenvolvemos um projeto para controle e acompanhamento da área de Help Desk. Vamos partir desde a criação da base de dados de exemplo até o desenvolvimento e aplicação dos indicadores.

## Visão Geral

Este projeto objetiva explorar e análisar e gerar indicadores para uma base de dados de chamados em um sistema de Help Desk. 

A gestão de chamados, seus SLAS e métricas é muito importante para controle da qualidade operacional de uma empresa, visto que praticamente todos os projetos de uma empresa necessitam, em algum momento, do suporte da área de Infra / help desk, talvez para alguma aprovação de acesso, resolução de problema em algum equipamento físico(hardware) ou instalação/configuração de software. 

## Objetivo Principal

Desenvolver e implementar indicadores que possibilitem aos gestores o monitoramento do:
- Tempo de atendimento
- Ciclo de atendimento
- Problemas mais recorrentes
- Áreas que mais demandam
- Demais oportunidades de Melhoria


## Metodologia

Para o desenvolvimento deste projeto foram propostos os seguintes passos:

01. Geração de uma base de dados de exemplo.
02. Preparação e Validação da base de dados. ( base poderá ser compartilhada no Kaggke para uso da comunidade)
03. Exploração das distribuições e validação se a base é fáctivel com mundo real e praticável.
04. Sugestão e desenvolvimento dos indicadores
05. Aplicação e validação dos indicadores

## Modelo de Dados

Utilizando a biblioteca [Faker]() do python vamos gerar alguns conjuntos de dados (tabelas), a serem utilizados na nossa análise, sendo eles:
. Funcionários: Registro dos funcionários com id, status, cargo e outros.
. Departamentos: Subseções da empresa
. Diretórias: Seções principais na empresa
. Chamados: Registro histórico dos chamados abertos no Help Desk a partir de 2020
. Problemas: Tipos de problemas a serem relacionados ao chamados


![](./docs/images/MER_tabelas.svg)