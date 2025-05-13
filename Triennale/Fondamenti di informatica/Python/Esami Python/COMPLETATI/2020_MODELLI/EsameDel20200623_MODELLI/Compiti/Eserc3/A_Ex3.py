from tester import tester_fun

import re

def A_Ex3(file):
    d = {}
    f = open(file, "r", encoding = "utf-8").read()
    pattern = r"<\w (\w+)='([^']+)'>"
    find = re.finditer(pattern, f, flags = re.MULTILINE)
    for match in find:
        print (match.group())
        attr = match.group(1)
        arg = match.group(2)
        d[attr] = d.get(attr, set())
        d[attr].add(arg)
    return d

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ["file1.txt"],{'nome': {'Marco Rossi', 'Mario Bianchi'},'indirizzo':{'viale dei Gladiatori'}})
counter_test_positivi += tester_fun(A_Ex3, ["file2.txt"],{'eta': {'30', '25'}, 'citta': {'Roma'}, 'auto': {'BMW'}})
counter_test_positivi += tester_fun(A_Ex3, ["file3.txt"],{'nome': {'Michele Bianchi'}, 'descrizione': {'Romaratona'}, 'posizione': {'1'}})
counter_test_positivi += tester_fun(A_Ex3, ["file4.txt"],{})
counter_test_positivi += tester_fun(A_Ex3, ["file5.txt"],{'eta': {'80'}, 'descrizione': {'Romaratona'}, 'posizione': {'789'}, 'stato': {'buono'}})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

