def Ex3(file):
    f=open(file,'r',encoding='UTF-8')
    diz1={} # dizionario per memorizzare il saldo del cc
    diz2={} # dizionario per memorizzare il numero di prelievi in rosso
    for riga in f:
        riga=riga.strip().split(',')
        nome=riga[0]
        cifra=int(riga[1])
        diz1[nome]=diz1.get(nome,0)+cifra
        if diz1[nome]<0:
            diz2[nome]=diz2.get(nome,0)+1
    f.close()
    massimo=0
    kmax=''
    for k in diz2:
        if diz2[k]>massimo:
            massimo=diz2[k]
            kmax=k
        elif diz2[k]==massimo and k<kmax:
            kmax=k
    if massimo==0: # non ci sono prelievi in rosso
        return 'nessun prelievo in rosso'
    else:
        return kmax,diz1[kmax]
           
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10
    
    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi1.csv'],('Antonio',-150))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi2.csv'],('Marco', 0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi3.csv'],'nessun prelievo in rosso')
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi4.csv'],('Gianni',0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi5.csv'],('Debora',20))
    
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi6.csv'],('Luca',-100))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi7.csv'],('Franco', 0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi8.csv'],'nessun prelievo in rosso')
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi9.csv'],('Giorgio',0))
    counter_test_positivi += tester_fun(Ex3, ['prelievi-depositi10.csv'],('Gianni',-400))


    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
