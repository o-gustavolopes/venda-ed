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
        return None
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

def criar_arquivo():
    arquivo_binario = "arquivo_binario.bin"

    try:
        with open(arquivo_binario, 'wb') as arquivo:
            pass
        print(f"\nArquivo binário '{arquivo_binario}' criado com sucesso!\n")
    except Exception as e:
        print(f"\nOcorreu um erro ao criar o arquivo binário: {e}\n")

    menu_opt()

def incluir_vendedor():
    try:
        codigo_vendedor = int(input("\nDigite o código do vendedor: "))
        codvend_bytes = codigo_vendedor.to_bytes((codigo_vendedor.bit_length() + 7) // 8, 'big')

        with open('arquivo_binario.bin', 'wb') as arquivo:
            arquivo.write(codvend_bytes)
        print("Vendedor incluído com sucesso!")
    except ValueError:
        print("O código precisa ser um número inteiro.")

def excluir_vendedor():
    pass


if __name__ == '__main__':
    menu_opt()
