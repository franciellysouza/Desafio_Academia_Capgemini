#contem a modelagem do anuncio
from datetime import datetime

class Anuncio(object):
    #todos os atributos da classe sao privados
    def __init__(self, nome, cliente, data_inicio, data_termino, invs_dia):
        self.__nome = nome
        self.__cliente = cliente
        #todas as datas a serem recebidas devem ser String no formato (dia-mes-ano), onde o ano contem 4 digitos
        self.__data_inicio = data_inicio
        self.__data_termino = data_termino
        self.__invs_dia = float(invs_dia)

    #retorna o nome do anuncio
    def get_nome(self):
        return self.__nome
    
    #retorna o ciente
    def get_cliente(self):
        return self.__cliente

    #retorna data inicio
    def get_inicio(self):
        return datetime.strptime(self.__data_inicio, "%d-%m-%Y")

    #retorna data termino
    def get_termino(self):
        return datetime.strptime(self.__data_termino, "%d-%m-%Y")

    #retorna o relatorio do anuncio
    def relatorio(self):
        #valor total investido
        #diferença de dias entre as datas de inicio e termino
        inicio = datetime.strptime(self.__data_inicio, "%d-%m-%Y")
        termino = datetime.strptime(self.__data_termino, "%d-%m-%Y")
        diferenca_datas = (termino-inicio).days

        
        total_investido =  diferenca_datas*self.__invs_dia

        #calcula a quantidade maxima de visulizacoes
        #pessoas que visualizam o anuncio original
        v_original = 30*total_investido
        #cliques no anuncio
        cliques = int(v_original/100*12)
        #compartilhamentos
        comp = int(cliques/20*3)
        #novas visluzalizacoes
        v_novas = comp*40
        #total de visulizacoes
        v_total = v_original+v_novas

        #considerando o máximo de 4 compartilhamentos
        v_total = v_total + v_total*40

        #calcula a quantidade maxima de cliques
        #a cada 100 pessoas que visulizam o anuncio 12 clicam nele
        cliques = int(v_total/100*12)

        #calcula a quantidade maxima de compartilhamentos
        #a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais
        comp = int(cliques/20*3)

        msg = "Anúncio {} possui {} reais investidos, obterá um total de {} visualizações, {} cliques e {} compartilhamentos".format(self.get_nome(), total_investido, v_total, cliques, comp)
        return msg
