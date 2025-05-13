from tester import tester_fun

def A_Ex1(s1, s2):
    i = 0
    ris=''
    while i<min(len(s1),len(s2)) and s1[i]==s2[i]:
        ris+=s1[i]
        i = i+1        
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ["amaca","amato"],"ama")
counter_test_positivi += tester_fun(A_Ex1, ["pippo","minnie"], "")
counter_test_positivi += tester_fun(A_Ex1, ["","pippo"], "")
counter_test_positivi += tester_fun(A_Ex1, ["arte","arteria"] ,"arte")
counter_test_positivi += tester_fun(A_Ex1, ["amato","ama"] ,"ama")

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

