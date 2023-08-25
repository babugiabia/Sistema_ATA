import csv

def pesquisar_usuario(usuario):
    cadastro_csv = open('cadastro.csv')

    dados = csv.DictReader(cadastro_csv, delimiter= ';')
   

    for usuario in dados:
        if usuario["nome"].lower() == nome.lower():
            matricula = usuario["matricula"]
            nome = usuario["nome"]
            return (True, nome, matricula)
            break
    return (False,)


