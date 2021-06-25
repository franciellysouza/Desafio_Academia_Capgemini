def calcula_anuncio(valor):
    #pessoas que visualizam o anuncio original
    v_original = 30*valor
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

    return v_total

invs = input("Informe o valor investido no anúncio: ")
print(calcula_anuncio(invs))