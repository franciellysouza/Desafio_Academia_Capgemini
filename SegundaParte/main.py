from anuncios import Anuncios
from anuncio import Anuncio

#cria a lista de anuncios
anuncios = Anuncios()
while(True):
    #menu de opcoes
    print("Menu de opções:\nDigite 1 para criar anúncio\n"
                +"Digite 2 para filtrar anúncios\n"
                +"Digite 3 para encerrar a execução da aplicação\n")

    result = input()
    if result == '1':
    #dados do anuncio
        nome = input("Informe o nome do anúncio: ")
        cliente = input("Informe o nome do cliente dono anúncio: ")
        inicio = input("Informe a data de início do anúncio no formato 'dia-mes-ano' onde o ano deve conter 4 dígitos: ")
        termino = input("Informe a data de término do anúncio no formato 'dia-mes-ano' onde o ano deve conter 4 dígitos: ")
        invs_dia = input("Informe o valor investido por dia no anúncio: ")

        anuncio = Anuncio(nome, cliente, inicio, termino, invs_dia)
        anuncios.add_anuncio(anuncio)

        print("Relatorio de anúncio: {}\n".format(anuncio.relatorio()))
    #filtrar relatorios
    elif result == '2':
        if len(anuncios.get_lista())>0 :
            filtro = input("Deseja filtrar os resultados por intervalo de tempo ou cliente?\n 'Digite 1 para intervalo de tempo ou 2 para cliente.\n")
            if filtro == '1':
                d_inicio = input("Informe a data de início do intervalo no formato 'dia-mes-ano' onde o ano deve conter 4 dígitos: ")
                d_termino = input("Informe a data de término do intervalo no formato 'dia-mes-ano' onde o ano deve conter 4 dígitos: ")
                resultado = anuncios.filtro_data((d_inicio, d_termino))
            elif filtro == '2':
                d_cliente = input("Informe o nome do cliente: ")
                resultado = anuncios.filtro_cliente(d_cliente)

            for relatorio in resultado:
                print(relatorio)
        else: 
            print("Nenhum anúncio cadastrado.\n")
    elif result == '3':
        break