from tester import tester_fun

def A_Ex4(file1,file2):
    f1 = open(file1,encoding='UTF-8')
    ranking={}  
    numRiga=0
    for riga in f1:
        numRiga+=1
        tennista = riga.strip()
        ranking[tennista]=numRiga   #posizioni più alte nel ranking
                                    #sono associate a numeri inferiori
    f1.close()
    f2 = open(file2,encoding='UTF-8')

    vincitori={}    #chiave:tennista che ha vinto almeno un incontro
                    #valore:insieme dei tennisti sconfitti dal tennista chiave

    daRestituire=set() #insieme di tennisti che hanno sconfitto almeno un tennista
                       #con posizione più alta nel ranking
    for riga in f2:
        dati = riga.strip().split(',')
        gioc1=dati[0].strip()
        gioc2=dati[1].strip()
        set1=int(dati[2])
        set2=int(dati[3])
        if set1>set2:
            if gioc1 in vincitori:
                vincitori[gioc1].add(gioc2)
            else:
                vincitori[gioc1]={gioc2}
            if ranking[gioc1]>ranking[gioc2]:
                daRestituire.add(gioc1)
        else:
            if gioc2 in vincitori:
                vincitori[gioc2].add(gioc1)
            else:
                vincitori[gioc2]={gioc1}
            if ranking[gioc2]>ranking[gioc1]:
                daRestituire.add(gioc2)
    #di seguito da vincitori tutti i tennisti che non sono da retituire
    for k in ranking:
        if k in vincitori and k not in daRestituire:
            vincitori.pop(k)
    return vincitori

                       

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri1.csv'],{'Federer':{ 'Medvedev', 'Djokovic'}, 'Nadal':{ 'Federer', 'Djokovic'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri2.csv'],{'Federer':{ 'Medvedev', 'Thiem','Djokovic'},'Nadal':{ 'Federer', 'Djokovic'},'Thiem':{'Nadal'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri3.csv'],{'Medvedev':{ 'Federer'},'Thiem':{ 'Nadal'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking2.csv','incontri4.csv'],{'Paperoga':{ 'Paperino'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking2.csv','incontri5.csv'],{'Paperoga':{ 'Pippo','Paperino'},'Pippo':{'Topolino','Paperoga'}})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
