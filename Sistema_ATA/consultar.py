import os
import csv

def consultar_ata(nome_reuniao):
    ata_csv = open('ata.csv')
    dados_ata = csv.DictReader(ata_csv, delimiter= ';')
   

    for ata in dados_ata:
        if ata["Nome da Reunião"].lower() == nome_reuniao.lower():
            data_reuniao = (ata["Data da Reunião"])
            participantes = (ata["Participantes"])
            topicos = (ata["Tópicos Debatidos"])
            return (True, data_reuniao, participantes, topicos)
            break
    return (False,)
