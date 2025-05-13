from tester import tester_fun

import re

def A_Ex3(file):
    f = open(file,encoding='UTF-8')
    diz = {}
    testo=f.read()
    pattern=r'\b\d+\b'
    matches = re.finditer(pattern,testo)
    for m in matches:
        i = int(m.group())
        if i in diz:
            diz[i]+=1
        else:
            diz[i]=1
    return diz

    

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ["file1.txt"],{123:3,150:2,1000:1,500:2})
counter_test_positivi += tester_fun(A_Ex3, ["file2.txt"],{1000:3,2000:2,450:2,1:1,2:1,0:1})
counter_test_positivi += tester_fun(A_Ex3, ["file3.txt"],{17:3,13:2,4:1,23:1,1:1})
counter_test_positivi += tester_fun(A_Ex3, ["file4.txt"],{125:2,25:2,150:2,5:3,1:1})
counter_test_positivi += tester_fun(A_Ex3, ["file5.txt"],{2021:2,10:1})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

