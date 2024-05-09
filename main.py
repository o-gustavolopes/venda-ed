# Estrutura de Dados tarefa
# Data de entrega: 04/09
# Alunos:
# 1- João Victor Ricardo Dias Leal
# 2- Gustavo Lopes Martins

import struct

registro_format = "if8s"  # Integer (4 bytes), Float (4 bytes), String (8 bytes)


def menu_opt():
    print("1 - Criar o arquivo de dados")
    print("2 - Incluir um determinado vendedor no arquivo")
    print("3 - Excluir um determinado vendedor no arquivo")
    print("4 - Alterar o valor total da venda de um determinado vendedor de um determinado mês")
    print("5 - Imprimir os registros na saída padrão")
    print("6 - Consultar o vendedor com maior valor da venda")
    print("7 - Finalizar o programa")

    usr_opt = input("\nDigite uma opção válida: ")

    if usr_opt == '1':
        criar_arquivo()
    elif usr_opt == '2':
        incluir_vendedor()
    elif usr_opt == '3':
        excluir_vendedor()
    elif usr_opt == '4':
        alterar_valor_venda()
    elif usr_opt == '5':
        imprimir_registros()
    elif usr_opt == '6':
        consultar_maior_venda()
    elif usr_opt == '7':
        print("Saindo...")
    else:
        print("Opção inválida")
        menu_opt()


def criar_arquivo():
    try:
        with open('arquivo_vendas.bin', 'wb'):
            print("Arquivo de dados criado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo de dados: {e}")

    menu_opt()


def incluir_vendedor():
    try:
        codigo_vendedor = int(input("Digite o código do vendedor: "))
        valor_venda = float(input("Digite o valor da venda: "))
        mes_ano = input("Digite o mês e ano (mm/aaaa): ")

        with open('arquivo_vendas.bin', 'ab') as arquivo:
            registro = struct.pack(registro_format, codigo_vendedor, valor_venda, mes_ano.encode())
            arquivo.write(registro)

        print("Vendedor incluído com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao incluir o vendedor: {e}")

    menu_opt()


def excluir_vendedor():
    try:
        codigo_vendedor = int(input("Digite o código do vendedor que deseja excluir: "))
        mes_ano = input("Digite o mês e ano do registro que deseja excluir (mm/aaaa): ")

        # Verifica se o formato do mês e ano é válido
        if len(mes_ano) != 7 or mes_ano[2] != '/' or not mes_ano[:2].isdigit() or not mes_ano[3:].isdigit():
            print("Formato de mês e ano inválido. Use o formato mm/aaaa.")
            menu_opt()
            return

        # Separa o mês e o ano
        mes, ano = mes_ano.split('/')
        mes = int(mes)
        ano = int(ano)

        vendedor_encontrado = False

        with open('arquivo_vendas.bin', 'r+b') as arquivo:
            while True:
                registro = arquivo.read(struct.calcsize(registro_format))
                if not registro:
                    break
                registro_data = struct.unpack(registro_format, registro)
                registro_mes, registro_ano = map(int, registro_data[2].decode().rstrip('\x00').split('/'))
                if registro_data[0] == codigo_vendedor and registro_mes == mes and registro_ano == ano:
                    arquivo.seek(-struct.calcsize(registro_format), 1)
                    arquivo.write(b'\x00' * struct.calcsize(registro_format))
                    print("Vendedor excluído com sucesso!")
                    vendedor_encontrado = True
                    break

            if not vendedor_encontrado:
                print("Vendedor não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro ao excluir o vendedor: {e}")

    menu_opt()


def alterar_valor_venda():
    try:
        codigo_vendedor = int(input("Digite o código do vendedor que deseja alterar: "))
        mes_ano = input("Digite o mês e ano do registro que deseja alterar (mm/aaaa): ")
        novo_valor = float(input("Digite o novo valor da venda: "))

        # Verifica se o formato do mês e ano é válido
        if len(mes_ano) != 7 or mes_ano[2] != '/' or not mes_ano[:2].isdigit() or not mes_ano[3:].isdigit():
            print("Formato de mês e ano inválido. Use o formato mm/aaaa.")
            menu_opt()
            return

        # Separa o mês e o ano
        mes, ano = mes_ano.split('/')
        mes = int(mes)
        ano = int(ano)

        vendedor_encontrado = False

        with open('arquivo_vendas.bin', 'r+b') as arquivo:
            while True:
                registro = arquivo.read(struct.calcsize(registro_format))
                if not registro:
                    break
                registro_data = struct.unpack(registro_format, registro)
                registro_mes, registro_ano = map(int, registro_data[2].decode().rstrip('\x00').split('/'))
                if registro_data[0] == codigo_vendedor and registro_mes == mes and registro_ano == ano:
                    novo_registro = struct.pack(registro_format, codigo_vendedor, novo_valor, registro_data[2])
                    arquivo.seek(-struct.calcsize(registro_format), 1)
                    arquivo.write(novo_registro)
                    print("Valor da venda alterado com sucesso!")
                    vendedor_encontrado = True
                    break

            if not vendedor_encontrado:
                print("Vendedor não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro ao alterar o valor da venda: {e}")

    menu_opt()


def imprimir_registros():
    try:
        with open('arquivo_vendas.bin', 'rb') as arquivo:
            while True:
                registro = arquivo.read(struct.calcsize(registro_format))
                if not registro:
                    break
                registro_data = struct.unpack(registro_format, registro)
                print(f"Código do vendedor: {registro_data[0]}, Valor da venda: {registro_data[1]}, "
                      f"Mês e ano: {registro_data[2].decode()}")
    except Exception as e:
        print(f"Ocorreu um erro ao imprimir os registros: {e}")

    menu_opt()


def consultar_maior_venda():
    try:
        maior_venda = None
        with open('arquivo_vendas.bin', 'rb') as arquivo:
            while True:
                registro = arquivo.read(struct.calcsize(registro_format))
                if not registro:
                    break
                registro_data = struct.unpack(registro_format, registro)
                if maior_venda is None or registro_data[1] > maior_venda[1]:
                    maior_venda = registro_data
        if maior_venda:
            print(f"Vendedor com maior valor de venda: Código: {maior_venda[0]}, Valor: {maior_venda[1]}, "
                  f"Mês e ano: {maior_venda[2].decode()}")
        else:
            print("Não há registros de vendas.")
    except Exception as e:
        print(f"Ocorreu um erro ao consultar o vendedor com maior valor de venda: {e}")

    menu_opt()


if __name__ == '__main__':
    menu_opt()
