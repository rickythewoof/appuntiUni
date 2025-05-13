from tester import tester_fun

def D_Ex3(l1,l2):
    ris=[]
    for i in range(len(l1)):
        inserisci=True
        for j in range(len(l1[i])):
            if j<len(l1[i])-1 and l1[i][j]!=l2[i][j+1]:
                inserisci=False
            elif j==len(l1[i])-1 and l1[i][j]!=l2[i][0]:
                inserisci=False
        if inserisci:
            ris.append(l1[i])
    ris.sort()
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex3, [["mamma", "asso", "re"],["amamm", "lago", "er"]],["mamma", "re"])
counter_test_positivi += tester_fun(D_Ex3, [["sara","osso"],["asar","ooss"]],["osso","sara"])
counter_test_positivi += tester_fun(D_Ex3, [["sara"],["rasa"]],[])
counter_test_positivi += tester_fun(D_Ex3, [["a"],["a"]],["a"])
counter_test_positivi += tester_fun(D_Ex3, [["a"],["A"]],[])

print('La funzione',D_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

