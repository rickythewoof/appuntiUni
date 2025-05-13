from tester import tester_fun

import re

def A_Ex1(file):
    testo = open(file,'r',encoding = 'UTF-8').read()
    pattern = r'http://(\w+\.)?(\w+)\.\w+([\w/]*)?'
    i = re.finditer(pattern,testo)
    insieme = set()
    for m in i:
        dominio = m.group(2)
        insieme.add(dominio)
    return insieme

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["file1.txt"],{'apple', 'google', 'gmail'})
counter_test_positivi += tester_fun(A_Ex1, ["file2.txt"],{'apple', 'google', 'gmail', 'microsoft'})
counter_test_positivi += tester_fun(A_Ex1, ["file3.txt"],{'apple', 'google', 'gmail', 'microsoft'})
counter_test_positivi += tester_fun(A_Ex1, ["file4.txt"],{'microsoft', 'apple', 'gmail', 'google', 'wikipedia'})
counter_test_positivi += tester_fun(A_Ex1, ["file5.txt"],{'microsoft', 'apple', 'gmail', 'google', 'wikipedia', 'wikimedia'})

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

