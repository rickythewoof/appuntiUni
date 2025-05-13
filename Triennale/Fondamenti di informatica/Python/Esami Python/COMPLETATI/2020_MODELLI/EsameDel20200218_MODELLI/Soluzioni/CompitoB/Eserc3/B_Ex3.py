from tester import tester_fun
import re

def B_Ex3(file,diz):
    f=open(file,'r',encoding='UTF-8')
    testo=f.read()
    ris=set()
    pattern = r'\b([0-9]{5,9}) \(([A-Z][A-Za-z]*)\)'
    i=re.finditer(pattern,testo)
    for m in i:
        if m.group(2) in diz:
            ris.add(diz[m.group(2)]+m.group(1))
    return ris

#### Soluzione che non fa uso di espressioni regolari
##
##def B_Ex3(file,diz):
##    f=open(file,'r',encoding='UTF-8')
##    testo=f.read()
##    ris=set()
##    lista = testo.split()
##    for i in range(len(lista)-1):
##        if lista[i].isdigit() and 5 <= len(lista[i]) <= 9 and lista[i+1][0]=='(' and lista[i+1][-1]==')':
##            nazione=lista[i+1][1:len(lista[i+1])-1]
##            if nazione in diz:
##                ris.add(diz[nazione]+lista[i])
##    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt',{'Francia':'0033','Italia':'0039'}] ,{'0033056784435'})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt',{'Spagna':'0034','Italia':'0039','UK':'0044'}],{'004411234', '003933445567'})
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt',{'Spagna':'0034','Italia':'0039'}] ,{'003933445567', '0034772749270'})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt',{'Germania':'0049','Italia':'0039'}] ,{'003933445566', '0049223345'})
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt',{'Germania':'0049','UK':'0044'}] ,set())

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

