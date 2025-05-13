from re import L
from tester import tester_fun

def A_Ex3(l):
    maxUpper = 0
    sol = []
    for elem in l:
        localUpper = 0
        for char in elem:
            if char.isupper():
                localUpper += 1
        maxUpper = max(maxUpper,localUpper)
    print (maxUpper)
    for elem in l:
        localUpper = 0
        for char in elem:
            if char.isupper():
                localUpper += 1
        if localUpper < maxUpper:
            sol.append(elem)
    return sol


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, [["piPPo", "pippo","PLuto","Pippo"]],["pippo","Pippo"])
counter_test_positivi += tester_fun(A_Ex3, [["Maria", "mamma","Monica"]] ,["mamma"])
counter_test_positivi += tester_fun(A_Ex3, [["","questa è una stringa"]] ,[])
counter_test_positivi += tester_fun(A_Ex3, [["Ciao","ciao"]] ,["ciao"])
counter_test_positivi += tester_fun(A_Ex3, [["gennaio","FEbbraio","Marzo"]] ,["gennaio","Marzo"])

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
