
from tester import tester_fun

import re

def A_Ex3(file):
    f = open(file, "r", encoding = "UTF-8")
    d = {}
    pattern = r"\w*\d+\w*"
    for riga in f:
        riga = riga.strip()
        print(repr(riga))
        finds = re.finditer(pattern, riga, flags=re.MULTILINE)
        for match in finds:
            isNumber = True
            num = (match.group())
            for char in num:
                if char.isalpha():
                    isNumber = False
            if isNumber:
                print("MATCH",match.group())
                num = int(num)
                d[num] = d.get(num, 0)
                d[num] += 1
    return d
    

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

