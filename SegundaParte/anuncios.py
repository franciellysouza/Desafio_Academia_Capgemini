#classe destinada a criação de anuncios e armazenamento dos mesmos em uma lista
from anuncio import Anuncio
from datetime import datetime
class Anuncios(object):

    def __init__(self):
        self.__lista = []

    #adiciona anuncio a lista
    def add_anuncio(self, anuncio):
        self.__lista.append(anuncio)

    #retorna de lista de anuncios
    def get_lista(self):
        return self.__lista

    #filtrar relatorios por intervalo de tempo
    def filtro_data(self, chave):
        #o campo 'anuncios' corresponde a uma lista de anuncios
        #o campo 'chave' ao intervalo de tempo. O campo é uma tupla no formato (data-inicio, data-fim)
        resultado = []
        try:
            inicio = datetime.strptime(chave[0], "%d-%m-%Y")
            termino = datetime.strptime(chave[1], "%d-%m-%Y")
        except:
            return "Datas Inválidas"

        for anuncio in self.__lista:
            #verifica se o intervalo do anuncio pertente ao intervalo de datas
            if anuncio.get_termino()<=termino and anuncio.get_inicio()>=inicio:
                #adiciona o anuncio a lista de resultados
                resultado.append(anuncio.relatorio())
        return resultado


    #filtrar relatorios por cliente
    def filtro_cliente(self, chave):
        #o campo 'anuncios' corresponde a uma lista de anuncios
        #o campo 'chave' ao cliente
        resultado = []
        for anuncio in self.__lista:
                #verifica se o intervalo do anuncio pertente ao cliente
                if anuncio.get_cliente()==chave:
                    #adiciona o anuncio a lista de resultados
                    resultado.append(anuncio.relatorio())
        return resultado

