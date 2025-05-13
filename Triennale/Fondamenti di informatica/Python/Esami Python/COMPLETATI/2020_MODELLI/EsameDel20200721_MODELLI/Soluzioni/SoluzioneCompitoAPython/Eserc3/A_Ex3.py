from tester import tester_fun

import re

def A_Ex3(file, c1, c2):
    testo = open(file,encoding='UTF-8').read()
    pattern= r"\b\w*"+c1+r"(\w\w)*"+c2+r"\w*\b"
    lista=testo.split()
    output=set()
    it = re.finditer(pattern,testo)
    for m in it:
        output.add(m.group())
    return output

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ["file1.txt",'a','o'],{'associazione','arco','acronimo'})
counter_test_positivi += tester_fun(A_Ex3, ["file2.txt",'s','e'],{'esclude'})
counter_test_positivi += tester_fun(A_Ex3, ["file2.txt",'c','o'],{'caro','colle'})
counter_test_positivi += tester_fun(A_Ex3, ["file3.txt",'c','o'],{'colle', 'caro', 'cor', 'poco'})
counter_test_positivi += tester_fun(A_Ex3, ["file4.txt",'c','m'],{'lacrimammo','Cacciammo','credevamo'})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

