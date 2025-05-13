def Ex3(l,file):
    f=open(file,'r',encoding='UTF-8')
    diz={}
    f.readline() # consuma la prima riga
    massimo=0
    for riga in f:
        riga=riga.strip().split(',')
        giocatore1=riga[0]
        giocatore2=riga[1]
        punto1=riga[2]
        punto2=riga[3]
        if l.index(punto1)>l.index(punto2):
            diz[giocatore1]=diz.get(giocatore1,0)+1
            if diz[giocatore1]>massimo:
                massimo=diz[giocatore1]
        else:
            diz[giocatore2]=diz.get(giocatore2,0)+1
            if diz[giocatore2]>massimo:
                massimo=diz[giocatore2]
    #print(massimo)
    ris=[]
    for k in diz:
        if diz[k]==massimo:
            ris.append(k)
    ris.sort()
    return ris
           
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10
    
    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file1.csv'],['Aldo','Marco'])
    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file2.csv'],['Anna'])
    counter_test_positivi += tester_fun(Ex3, [['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci'],'file3.csv'],['Anna','Franco','Olga'])
    counter_test_positivi += tester_fun(Ex3, [['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci'],'file4.csv'],['Matteo'])
    counter_test_positivi += tester_fun(Ex3, [['sballato','mezzo','uno','uno e mezzo','due','due e mezzo','tre','tre e mezzo','quattro', 'quattro e mezzo','cinque','cinque e mezzo','sei','sei e mezzo','sette','sette e mezzo'],'file5.csv'],['Frank','Olga'])
    
    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file6.csv'],['Aldo','Marco']) # due giocatori che vincono entrambi il massimo numero di volte
    counter_test_positivi += tester_fun(Ex3, [['uno','due','tre'],'file7.csv'],['Massimo']) # una sola partita
    counter_test_positivi += tester_fun(Ex3, [['A','B','C','D'],'file8.csv'],['Luca']) # un solo vincitore
    counter_test_positivi += tester_fun(Ex3, [['giu','su'],'file9.csv'],['Adele', 'Ernesto', 'Franco', 'Mimmo']) # tutti vincitori con una vittoria
    counter_test_positivi += tester_fun(Ex3, [['a','b','c','d','e'],'file10.csv'],['Carlo', 'Enrico']) # due vincitori su diversi

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
