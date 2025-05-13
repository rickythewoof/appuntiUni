def Ex3(file,n):
    diz = {}
    lista = []
    postidisp = n
    f = open(file,'r',encoding='UTF-8')
    for riga in f:
        dati = riga.strip().split(',')
        nome = dati[0]
        tipo = dati[1]
        if tipo == 'P':
            numero = int(dati[2])
            if numero <= postidisp:
                diz[nome] = numero
                postidisp -= numero
            else:
                lista.append((nome,numero))
        if tipo == 'C':
            postidisp += diz.pop(nome)
            for elem in lista:
                if elem[1] <= postidisp:
                    diz[elem[0]]= elem[1]
                    lista.remove(elem)
                    postidisp -= elem[1]      
    f.close()
    return diz

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['prenotazioni1.csv',10],{'Marco': 4, 'Giorgio': 5})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni1.csv',8],{'Marco': 4, 'Paola': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni2.csv',12],{'Giorgio': 3, 'Andrea': 3, 'Paola': 6})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni2.csv',8],{'Giorgio': 3, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni3.csv',12],{'Paola': 6, 'Andrea': 3, 'Michela': 2})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['prenotazioni3.csv',15],{'Paola': 6, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni4.csv',8],{'Andrea': 3, 'Marco': 1, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni4.csv',14],{'Paola': 6, 'Andrea': 3, 'Marco': 1, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni5.csv',12],{'Paola': 6, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni5.csv',30],{'Paola': 6, 'Gianni': 7, 'Andrea': 3, 'Michela': 2})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
