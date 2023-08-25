import os
import csv


def cadastrar():
    dados =  {}
    os.system('cls') or None
    print("\n-------- CADASTRO DE USUÁRIO --------\n")

    
    nome = input("Nome: ")
    matricula = int(input("Matricula: "))
        

    dados [nome] = [matricula]
    colunas = ['nome', 'matricula']

    files_exists = os.path.isfile('cadastro.csv') 

    with open ('cadastro.csv', 'a', newline='', encoding='utf-8') as cadastro_csv:
        cadastrar = csv.DictWriter(cadastro_csv, fieldnames=colunas, delimiter=';', lineterminator='\r\n')
        if not files_exists:
            cadastrar.writeheader()
        cadastrar.writerow({'nome':nome.title(), 'matricula':matricula})
    print('Cadastro realizado com sucesso!')
