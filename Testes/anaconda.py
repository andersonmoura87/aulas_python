# INICIO DESCARGA FERTILIZANTES ETC
        barge_index_fertETC = -1
        if (~manutencao_carregamento_barcFertETC and
                collections.Counter(lista_abertura_posicao_barcacas[1])[
                    'Cheia ETC Fert.'] > 0 and barcacas_descarga_fertETC == 1):
            barcacas_descarga_fertETC = 1
            barge_index_fertETC = lista_abertura_posicao_barcacas[1].index('Cheia ETC Fert.')
            lista_abertura_posicao_barcacas[1][barge_index_fertETC] = 'Em Descarga ETC Fert.'
            # print('INÍCIO DE DESCARGA BARCAÇA FERTILIZANTE' , dt_simulacao )

        if (~manutencao_carregamento_barcFertETC and
                collections.Counter(lista_abertura_posicao_barcacas[1])[
                    'Em Descarga ETC Fert.'] > 0 and barcacas_descarga_fertETC):
            for i in lista_abertura_posicao_barcacas_aux[2:]:
                if (lista_abertura_posicao_barcacas[lista_abertura_posicao_barcacas_aux.index(i)][
                    barge_index_fertETC] > 0):
                    lista_descarga_fertilizantesETC[0].append(dt_simulacao)
                    lista_descarga_fertilizantesETC[1].append(min(taxa_descarga_fertETC,
                                                                  lista_abertura_posicao_barcacas[
                                                                      lista_abertura_posicao_barcacas_aux.index(i)][
                                                                      barge_index_fertETC]))
                    lista_descarga_fertilizantesETC[2].append(
                        lista_abertura_posicao_barcacas_aux[lista_abertura_posicao_barcacas_aux.index(i)])
                    lista_descarga_fertilizantesETC[3].append(nome_cenario)

                    lista_abertura_posicao_barcacas[lista_abertura_posicao_barcacas_aux.index(i)][
                        barge_index_fertETC] -= min(taxa_descarga_fertETC, lista_abertura_posicao_barcacas[
                        lista_abertura_posicao_barcacas_aux.index(i)][barge_index_fertETC])

                    break

            if verificarCargaBarcacaRetorno(barge_index_fertETC) == 0:
                barcacas_descarga_fertETC = 0
                print('Indice da Barcaça Fim Carregamento:'barge_index_fertETC')
                # print('DESCARGA BARCAÇA FERTILIZANTE REALIZADA' , dt_simulacao )
                lista_abertura_posicao_barcacas[1][barge_index_fertETC] = 'Vazia ETC'
        # FIM DESCARGA FERTILIZANTES ETC
