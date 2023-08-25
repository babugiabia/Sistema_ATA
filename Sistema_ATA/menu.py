import emitir, cadastro_usuario, consultar, listar 

resposta = 's'

while resposta == 's':

    menu = '''-------- EMISSOR DE ATA --------
    \r[1] Emitir Ata
    \r[2] Consultar Ata
    \r[3] Cadastrar Usuário
    \r[4] Listar Arquivos de ATA
    '''

    print(menu)
    opcao = int(input("Escolha a opção: "))

    if opcao == 1:
        emitir.emitir_ata()
    elif opcao == 2:
        break
        consultar.consultar_ata()
    elif opcao == 3:
        cadastro_usuario.cadastrar()
    elif opcao == 4:
        listar.arquivos_ata()
    else:
        print("\nOpção inválida!")

    resposta = input("\nDeseja continuar? [s/n]").lower()
    while resposta not in ['s', 'n']:
        resposta = input("Por favor, digite 's' para continuar ou 'n' para sair: ").lower()