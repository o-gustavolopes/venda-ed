def menu_opt():
    print("1 - Criar o arquivo de dados\n2 - Incluir um determinado vendedor no arquivo\n3 - Excluir um determinado "
          "vendedor no arquivo\n4 - Alterar o valor toral da venda de um determinado vendedor de um determinado "
          "mês\n5 - Imprimir os registros na saída padrão\n6 - Consultar o vendedor com maior valor da venda\n7 - "
          "Finalizar o programa")
    usr_opt = input("\nDigite uma opção válida: ")

    if usr_opt == '1':
        criar_arquivo()
    elif usr_opt == '2':
        incluir_vendedor()
    elif usr_opt == '3':
        excluir_vendedor()
    elif usr_opt == '4':
        return None
    elif usr_opt == '5':
        return None
    elif usr_opt == '6':
        return None
    elif usr_opt == '7':
        print("Saindo...")
    else:
        print("Opção inválida")
        menu_opt()

def criar_arquivo():
    arquivo = "arquivo.txt"

    try:
        with open(arquivo, 'w') as arq:
            pass
        print(f"\nArquivo '{arquivo}' criado com sucesso!\n")
    except Exception as e:
        print(f"\nOcorreu um erro ao criar o arquivo: {e}\n")

    menu_opt()

def incluir_vendedor():
    try:
        codigo_vendedor = int(input("\nDigite o código do vendedor: "))

        with open('arquivo.txt', 'a') as arquivo:
            arquivo.write(str(codigo_vendedor) + '\n')
        print("Vendedor incluído com sucesso!\n")
    except ValueError:
        print("O código precisa ser um número inteiro.")

    menu_opt()

def excluir_vendedor():
    cod_excluido = input("\nDigite o código do vendedor que deseja excluir (se quiser cancelar a operação digite zero): ")
    if cod_excluido == 0:
        print("Operação cancelada.\n")
        menu_opt()
    else:
        with open('arquivo.txt', 'r') as arquivo_leitura:
            linhas = arquivo_leitura.readlines()
            vendedor_encontrado = False
            for linha in linhas:
                partes = linha.strip().split(',')
                if partes[0] == cod_excluido:
                    vendedor_encontrado = True

            if not vendedor_encontrado:
                print("Código do vendedor não encontrado.")
                excluir_vendedor()
            else:
                with open('arquivo.txt', 'w') as arquivo_escrita:
                    for linha in linhas:
                        partes = linha.strip().split(',')
                        if partes[0] != cod_excluido:
                            arquivo_escrita.write(linha)
                print(f"Vendedor {cod_excluido} excluído com sucesso.\n")

    menu_opt()

def alterar_valores():
    pass

def print_registros():
    pass

def vendedor_maior_venda():
    pass


if __name__ == '__main__':
    menu_opt()
