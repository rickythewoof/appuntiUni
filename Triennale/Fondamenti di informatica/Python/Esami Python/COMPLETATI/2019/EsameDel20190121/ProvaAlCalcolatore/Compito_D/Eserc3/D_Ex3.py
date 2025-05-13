from tester import tester_fun

def D_Ex3(l1,l2):
    solution = l1.copy()
    print (solution)
    for wordIndex in range(len(l1)):
        print (wordIndex, l1[wordIndex], l2[wordIndex])
        if len(l1[wordIndex]) == 1:
            if l1[wordIndex] != l2[wordIndex]:
                solution.remove(l1[wordIndex])
        for charIndex in range(len(l1[wordIndex])-1):
            print(charIndex, l1[wordIndex][charIndex], l2[wordIndex][charIndex])
            if l1[wordIndex][-1] != l2[wordIndex][0]:
                solution.remove(l1[wordIndex])
                break
            elif l1[wordIndex][charIndex] != l2[wordIndex][charIndex+1]:
                solution.remove(l1[wordIndex])
                break
    solution.sort()
    return solution

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
