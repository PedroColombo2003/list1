"""
Titulo:Programa Lista
Autor: Pedro Colombo
Data: 03/03/2025
Versão: 0.0.1
Descrição: Esse resolve o seguinte problema: Escreva um programa que busque um determinado elemento em uma lista.Considere inicialmente a lista [1,5,-1,9]

"""
# Alocação de memória

lista = [1,5,-1,9]

#Entrada de dados

numero = int(input("Qual numero você gostaria de achar? "))

# Saida e processamento de dados

if numero in lista:
    print("Essse número está na lista")

else: print("Esse número não esta na lista")