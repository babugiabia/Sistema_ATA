import os, csv

def arquivos_ata():
    ata_csv = open('ata.csv', encoding='utf-8')
    dados = csv.DictReader(ata_csv,delimiter=';')

    os.system('cls') or None
    print('-------- LISTAGEM DE  ATAS ---------')
    print(f'{"REUNIÃO":15}', f'{"DATA":25}', "PARTICIPANTES", "TÓPICOS" )
    for ata in dados:
        print(f'{ata["Nome da Reunião"]:15}', f'{ata["Data da Reunião"]:25}', f'{ata["Participantes"]}',f'{ata["Tópicos Debatidos"]}')
    ata_csv.close()