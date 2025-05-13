from tester import tester_fun

def B_Ex3(l):
    maxLower = 0
    sol = []
    for elem in l:
        localLower = 0
        for char in elem:
            if char.islower():
                localLower += 1
        maxLower = max (maxLower, localLower)
    print(maxLower)
    for elem in l:
        sol.append(elem)
        localLower = 0
        for char in elem:
            if char.islower():
                localLower += 1
        if localLower == maxLower:
            sol.append(elem)
    return sol        

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, [["piPPo", "PIppO", "PLuto", "PiPPo"]] ,["piPPo", "piPPo", "PIppO","PLuto", "PLuto", "PiPPo"])
counter_test_positivi += tester_fun(B_Ex3, [["mamma", "pippo", "Pluto", "Pluto"]]  ,["mamma", "mamma", "pippo", "pippo", "Pluto", "Pluto"])
counter_test_positivi += tester_fun(B_Ex3, [["ACME", "ACM"]] ,["ACME","ACME", "ACM","ACM"])
counter_test_positivi += tester_fun(B_Ex3, [[""]] ,["",""])
counter_test_positivi += tester_fun(B_Ex3, [["ciao","ciao"]] ,["ciao","ciao","ciao","ciao"])

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

