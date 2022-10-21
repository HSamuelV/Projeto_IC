from dataclasses import replace
import pandas as pd
import re
import numpy as np
from collections import OrderedDict
from sympy import sring
import os

os.system('cls' if os.name == 'nt' else 'clear')


def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))


def remove_dups_for(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

# -------------- Filtragem arquivo nos_2 --------------

#ler o arquivo inicial
arquivo = pd.read_csv('nos_2.csv', sep=',', encoding='utf-8')

#trocar os não informados
arquivo[:] = arquivo[:].fillna('Não informado')

#Tirar número de coluna que deve ter apenas string
for i in range(len(arquivo)):
    if has_numbers(arquivo['cidade'][i]) == True:
        arquivo['cidade'][i] = 'Não informado'

#arrumar grande_area e area
# Replacing the strings "Subarea" and "Especialidade" with an empty string.
for i in range(len(arquivo)):
    if "Subarea" in arquivo['grande_area'][i]:
        arquivo['grande_area'][i] = arquivo['grande_area'][i].replace('Subarea',"")
    
    elif "Especialidade" in arquivo['area'][i]:
        arquivo['area'][i] = arquivo['area'][i].replace("Especialidade","")
    
    elif "Especialidade" in arquivo['grande_area'][i]:
        arquivo['grande_area'][i] = arquivo['grande_area'][i].replace("Especialidade","")


#tirar a linha com a titulação "Ensino" e linhas sem "grande_area" e "area"
# Removing rows where the column `titulacao` contains the word `Ensino`.
for i in range(len(arquivo)):
    if "Ensino" in arquivo['titulacao'][i]:
        arquivo = arquivo.drop([i])


#colocar apenas as areas que mais repetem

#criar arquivo filtrado 1
arquivo.to_csv('nos_3_filtro.csv', sep=',', encoding='utf-8',index=False)

#    ------- Filtragem de arquivo dados_formacao_academica_todos ------------

#ler o arquivo formação
arquivo_formacao = pd.read_csv('dados_formacao_academica_todos.csv',sep=',',encoding='utf-8')

#adicionar os não informados
arquivo_formacao[:] = arquivo_formacao[:].fillna('Não informado')

#criar arquivo filtrado 2
arquivo_formacao.to_csv('nos_filtro_formacao.csv',sep=',',encoding='utf-8',index=False)


