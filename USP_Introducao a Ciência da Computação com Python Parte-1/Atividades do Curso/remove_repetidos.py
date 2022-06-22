# remove_repetidos

'''
 Lista usada no teste :
 lista = [2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10]
 
'''




def remove_repetidos(lista):
    nova_lista = []
    for i in lista :
        if i not in nova_lista :
            nova_lista.append(i)
    return sorted(nova_lista)

