import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

        return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    modulos_soma = 0
    for i in range(6):
        modulos_soma += abs(as_a[i] - as_b[i])

    temp = modulos_soma / 6

    return temp


pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    sentencas = separa_sentencas(texto)

    frases = funcao_frases(sentencas)

    palavras = funcao_palavras(frases)

    temp = []

    temp.append(WAL(palavras))
    temp.append(TTR(palavras))
    temp.append(HLR(palavras))
    temp.append(SAL(sentencas))
    temp.append(SAC(sentencas, frases))
    temp.append(PAL(frases))

    return temp


pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    assinaturas = []

    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    graus_similaridade = []
    for assinatura in assinaturas:
        graus_similaridade.append(compara_assinatura(assinatura, ass_cp))

    temp = graus_similaridade.index(min(graus_similaridade)) + 1

    return temp


def WAL(palavras):
    palavra_tamanhoSoma = 0
    for palavra in palavras:
        palavra_tamanhoSoma += len(palavra)

    temp = palavra_tamanhoSoma / len(palavras)

    return temp


def TTR(palavras):
    return n_palavras_diferentes(palavras) / len(palavras)


def HLR(palavras):
    return n_palavras_unicas(palavras) / len(palavras)


def SAL(sentencas):
    sentenca_tamanhoSoma = 0
    for sentenca in sentencas:
        sentenca_tamanhoSoma += len(sentenca)

    temp = sentenca_tamanhoSoma / len(sentencas)

    return temp


def SAC(sentencas, frases):
    return len(frases) / len(sentencas)


def PAL(frases):
    frase_tamanhoSoma = 0
    for frase in frases:
        frase_tamanhoSoma += len(frase)

    return frase_tamanhoSoma / len(frases)


def funcao_frases(sentencas):
    frases_blocos = []
    for sentenca in sentencas:
        frases_blocos.append(separa_frases(sentenca))

    temp = []
    for frases_i in frases_blocos:
        for frases_j in frases_i:
            temp.append(frases_j)

    return temp


def funcao_palavras(frases):
    palavras_blocos = []
    for frase in frases:
        palavras_blocos.append(separa_palavras(frase))

    temp = []
    for palavras_i in palavras_blocos:
        for palavras_j in palavras_i:
            temp.append(palavras_j)

    temp.sort()

    return temp


pass
