import os
import csv
import pesquisar as p

def emitir_ata(): 
    os.system('cls')
    nome_reuniao = input("Nome da Reunião:")
    data_reuniao = input("Data da Reunião:")

    participantes = []
    topicos = []

    while True:
        participante = input("Nome de quem está redigindo a ATA: ")
        topico = input("Tópico Discutido [ou digite 'sair' para encerrar]: ")
        if topico.lower() == "sair":
            break
        participantes.append(participante)

    
    ata = {
        "Nome da Reunião": nome_reuniao,
        "Data da Reunião": data_reuniao,
        "Participantes": ','.join(participantes),
        "Tópicos Debatidos": ','.join(topicos)
    }

    arquivo_existe = os.path.isfile("ata.csv")
    with open("ata.csv", "a", newline="", encoding="utf-8") as arquivo_csv:
        emissor_csv = csv.DictWriter(arquivo_csv, fieldnames=ata.keys())

        if not arquivo_existe:

            emissor_csv.writerow(ata)

        
        print("ATA criada com sucesso!")



