from tester import tester_fun

import re

def A_Ex3(file, c1, c2):
    sol = set()
    f = open(file, "r", encoding="utf-8").read()
    pattern = f"\b\w*{c1}(\w\w)*{c2}\w*\b"
    find = re.finditer(pattern, f, flags = re.MULTILINE)
    for match in find:
        sol.add(match.group())
    return sol
    

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

